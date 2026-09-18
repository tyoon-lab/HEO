# heo_spatial_phase_field_gate_v2.py
# Date: 2026-09-18
#
# Spatial mechanism-sufficiency model for the HEO GITT project.
# This is NOT a uniquely identified material-parameter model.
#
# Free-energy density (dimensionless):
# f = c ln c + (1-c) ln(1-c)
#     + W phi^2(1-phi)^2
#     + K(c_tr-c)phi
#     + (kappa/2)|grad phi|^2
#
# mu = ln[c/(1-c)] - K phi
# dc/dt = -div(J),  J = -D_eff grad(mu)
# dphi/dt = -M_phi[2W phi(1-phi)(1-2phi)
#                  + K(c_tr-c) - kappa laplacian(phi)]
#
# Pulse/rest protocol: 600 s inward Li flux + 3600 s zero-flux rest.

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

class RadialPhaseField:
    def __init__(self, N=30, Ddim=0.0015, Mphi=0.015, cstar=0.60,
                 W=0.60, K=1.80, kappa=0.002, jin=2e-5):
        self.N=N; self.Ddim=Ddim; self.Mphi=Mphi; self.cstar=cstar
        self.W=W; self.K=K; self.kappa=kappa; self.jin=jin
        self.re=np.linspace(0.0,1.0,N+1)
        self.rc=0.5*(self.re[:-1]+self.re[1:])
        self.A=self.re**2
        self.V=(self.re[1:]**3-self.re[:-1]**3)/3.0

    @staticmethod
    def gp(phi):
        return 2.0*phi*(1.0-phi)*(1.0-2.0*phi)

    def lap(self,u):
        grad=np.zeros(self.N+1)
        grad[1:self.N]=(u[1:]-u[:-1])/(self.rc[1:]-self.rc[:-1])
        return (self.A[1:]*grad[1:]-self.A[:-1]*grad[:-1])/self.V

    def mu(self,c,phi):
        cc=np.clip(c,1e-6,1.0-1e-6)
        return np.log(cc/(1.0-cc))-self.K*phi

    def rhs(self,t,y,pulse):
        c=y[:self.N]
        phi=y[self.N:]
        mu=self.mu(c,phi)

        J=np.zeros(self.N+1)
        J[1:self.N]=-self.Ddim*(mu[1:]-mu[:-1])/(self.rc[1:]-self.rc[:-1])
        J[-1]=-self.jin if pulse else 0.0
        dc=-(self.A[1:]*J[1:]-self.A[:-1]*J[:-1])/self.V

        dG=(self.W*self.gp(phi)
            + self.K*(self.cstar-c)
            - self.kappa*self.lap(phi))
        dphi=-self.Mphi*dG

        # projected Allen-Cahn bounds
        dphi[(phi<=0.0)&(dphi<0.0)]=0.0
        dphi[(phi>=1.0)&(dphi>0.0)]=0.0

        return np.r_[dc,dphi]

    def voltage_proxy(self,y):
        c=y[:self.N]
        phi=y[self.N:]
        mu=self.mu(c,phi)
        return -np.sum(mu*self.V)/np.sum(self.V)

    def averages(self,y):
        c=y[:self.N]
        phi=y[self.N:]
        return (np.sum(c*self.V)/np.sum(self.V),
                np.sum(phi*self.V)/np.sum(self.V))

def run_gitt(model,ncycles=22,nrest=100):
    y=np.r_[np.full(model.N,0.10),np.zeros(model.N)]
    trest=np.unique(np.r_[0.0,3.0,np.geomspace(0.1,3600.0,nrest),3600.0])
    trest.sort()
    rows=[]
    vrests=[]

    for k in range(ncycles):
        sp=solve_ivp(
            lambda t,yy:model.rhs(t,yy,True),
            (0.0,600.0),y,method="BDF",
            rtol=5e-6,atol=2e-8,t_eval=[600.0],max_step=50.0
        )
        if not sp.success:
            raise RuntimeError(sp.message)
        yp=sp.y[:,-1]

        sr=solve_ivp(
            lambda t,yy:model.rhs(t,yy,False),
            (0.0,3600.0),yp,method="BDF",
            rtol=5e-6,atol=2e-8,t_eval=trest,max_step=80.0
        )
        if (not sr.success) or sr.y.shape[1] != len(trest):
            raise RuntimeError(sr.message)

        V=np.array([model.voltage_proxy(sr.y[:,i]) for i in range(sr.y.shape[1])])
        i3=np.argmin(np.abs(trest-3.0))
        amp=abs(V[-1]-V[i3])

        if amp>1e-12:
            F=abs((V-V[i3])/(V[-1]-V[i3]))
            ids=np.where((trest>=3.0)&(F>=0.632))[0]
            t63=trest[ids[0]]-3.0 if len(ids) else np.nan
        else:
            t63=np.nan

        y=sr.y[:,-1]
        cbar,phibar=model.averages(y)
        rows.append([k,cbar,phibar,amp,t63])
        vrests.append(V)

    return pd.DataFrame(
        rows,
        columns=["cycle","c_bar","phi_bar","relax_amp","t63_s"]
    ), trest, np.array(vrests)

def ensemble_run(cstars,weights,common_kwargs):
    dfs=[]
    Vsets=[]
    trest=None

    for cs in cstars:
        model=RadialPhaseField(cstar=float(cs),**common_kwargs)
        df,trest,V=run_gitt(model)
        dfs.append(df)
        Vsets.append(V)

    Vens=np.tensordot(weights,np.array(Vsets),axes=(0,0))
    i3=np.argmin(np.abs(trest-3.0))
    rows=[]

    for k in range(Vens.shape[0]):
        V=Vens[k]
        amp=abs(V[-1]-V[i3])
        if amp>1e-12:
            F=abs((V-V[i3])/(V[-1]-V[i3]))
            ids=np.where((trest>=3.0)&(F>=0.632))[0]
            t63=trest[ids[0]]-3.0 if len(ids) else np.nan
        else:
            t63=np.nan

        cbar=np.average([d.loc[k,"c_bar"] for d in dfs],weights=weights)
        phibar=np.average([d.loc[k,"phi_bar"] for d in dfs],weights=weights)
        rows.append([k,cbar,phibar,amp,t63])

    return pd.DataFrame(
        rows,
        columns=["cycle","c_bar","phi_bar","relax_amp","t63_s"]
    ), trest, Vens

def fwhm_state(df):
    x=df["c_bar"].to_numpy()
    y=df["relax_amp"].to_numpy()
    peak=y.max()
    ids=np.where(y>=peak/2.0)[0]
    return x[ids[-1]]-x[ids[0]] if len(ids)>1 else 0.0

def build_cases():
    HEO,_,_=run_gitt(RadialPhaseField(
        N=30,Ddim=0.0015,Mphi=0.015,cstar=0.60,
        W=0.60,K=1.80,kappa=0.002,jin=2e-5
    ))

    weights=np.array([0.1,0.2,0.4,0.2,0.1])

    BM,_,_=ensemble_run(
        np.array([0.48,0.54,0.60,0.66,0.72]),weights,
        dict(N=30,Ddim=0.0030,Mphi=0.012,
             W=0.50,K=1.60,kappa=0.002,jin=2e-5)
    )

    MG,_,_=run_gitt(RadialPhaseField(
        N=30,Ddim=0.0015,Mphi=0.001,cstar=0.79,
        W=0.80,K=1.80,kappa=0.002,jin=2e-5
    ))

    BMMG,_,_=ensemble_run(
        np.array([0.64,0.71,0.78,0.85,0.92]),weights,
        dict(N=30,Ddim=0.0030,Mphi=0.0008,
             W=0.70,K=1.70,kappa=0.002,jin=2e-5)
    )

    return {"HEO":HEO,"BM-HEO":BM,"Mg-HEO":MG,"BM-Mg-HEO":BMMG}

if __name__ == "__main__":
    cases=build_cases()
    rows=[]
    for name,df in cases.items():
        im=int(df["relax_amp"].idxmax())
        rows.append({
            "Sample":name,
            "Peak_dimensionless_relaxation":df.loc[im,"relax_amp"],
            "c_at_peak":df.loc[im,"c_bar"],
            "FWHM_in_c":fwhm_state(df),
            "t63_at_peak_min":df.loc[im,"t63_s"]/60.0,
            "Final_transformed_fraction":df.iloc[-1]["phi_bar"],
        })

    summary=pd.DataFrame(rows)
    print(summary.to_string(index=False))
    summary.to_csv("HEO_SPATIAL_PHASE_FIELD_GATE_V2_SUMMARY.csv",index=False)
