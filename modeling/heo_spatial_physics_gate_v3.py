# heo_spatial_physics_gate_v3.py
# HEO 1D spherical phase-field physics gate
# Date: 2026-09-18
# Purpose: mechanism sufficiency, NOT unique parameter identification.

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

class RadialPF:
    def __init__(self, N=24, Ddim=0.0015, Mphi=0.015, cstar=0.60,
                 W=0.60, K=1.80, kappa=0.002, jin=2e-5,
                 Gmg=0.0, Bel=0.20, ell_relief=0.08,
                 Ssurf=0.08, ell_wet=0.06):
        self.N=N; self.Ddim=Ddim; self.Mphi=Mphi; self.cstar=cstar
        self.W=W; self.K=K; self.kappa=kappa; self.jin=jin
        self.Gmg=Gmg; self.Bel=Bel; self.ell_relief=ell_relief
        self.Ssurf=Ssurf; self.ell_wet=ell_wet
        self.re=np.linspace(0,1,N+1)
        self.rc=0.5*(self.re[:-1]+self.re[1:])
        self.A=self.re**2
        self.V=(self.re[1:]**3-self.re[:-1]**3)/3
        d=1-self.rc
        self.qel=1-np.exp(-d/max(ell_relief,1e-6))
        self.wsurf=np.exp(-d/max(ell_wet,1e-6))

    @staticmethod
    def gp(phi):
        return 2*phi*(1-phi)*(1-2*phi)

    def lap(self,u):
        grad=np.zeros(self.N+1)
        grad[1:self.N]=(u[1:]-u[:-1])/(self.rc[1:]-self.rc[:-1])
        return (self.A[1:]*grad[1:]-self.A[:-1]*grad[:-1])/self.V

    def mu(self,c,phi):
        cc=np.clip(c,1e-6,1-1e-6)
        return np.log(cc/(1-cc))-self.K*phi

    def rhs(self,t,y,pulse):
        c=y[:self.N]; phi=y[self.N:]
        mu=self.mu(c,phi)
        J=np.zeros(self.N+1)
        J[1:self.N]=-self.Ddim*(mu[1:]-mu[:-1])/(self.rc[1:]-self.rc[:-1])
        J[-1]=-self.jin if pulse else 0.0
        dc=-(self.A[1:]*J[1:]-self.A[:-1]*J[:-1])/self.V

        # Free-energy derivative:
        # W*g(phi) + K(cstar-c)phi + Gmg*phi
        # + 0.5*Bel*qel(r)*phi^2 - Ssurf*wsurf(r)*phi
        # + 0.5*kappa*|grad phi|^2
        dG=(self.W*self.gp(phi)
            + self.K*(self.cstar-c)
            + self.Gmg
            + self.Bel*self.qel*phi
            - self.Ssurf*self.wsurf
            - self.kappa*self.lap(phi))
        dphi=-self.Mphi*dG
        dphi[(phi<=0)&(dphi<0)]=0
        dphi[(phi>=1)&(dphi>0)]=0
        return np.r_[dc,dphi]

    def voltage(self,y):
        c=y[:self.N]; phi=y[self.N:]
        mu=self.mu(c,phi)
        return -np.sum(mu*self.V)/np.sum(self.V)

    def avg(self,y):
        c=y[:self.N]; phi=y[self.N:]
        return np.sum(c*self.V)/np.sum(self.V), np.sum(phi*self.V)/np.sum(self.V)

def run(model,ncycles=22,nrest=70):
    y=np.r_[np.full(model.N,.10),np.zeros(model.N)]
    tr=np.unique(np.r_[0,3,np.geomspace(.1,3600,nrest),3600]); tr.sort()
    rows=[]; Vs=[]
    for k in range(ncycles):
        sp=solve_ivp(lambda t,yy:model.rhs(t,yy,True),(0,600),y,method="BDF",
                     rtol=7e-6,atol=3e-8,t_eval=[600],max_step=50)
        if not sp.success: raise RuntimeError(sp.message)
        yp=sp.y[:,-1]
        sr=solve_ivp(lambda t,yy:model.rhs(t,yy,False),(0,3600),yp,method="BDF",
                     rtol=7e-6,atol=3e-8,t_eval=tr,max_step=80)
        if not sr.success: raise RuntimeError(sr.message)
        V=np.array([model.voltage(sr.y[:,i]) for i in range(sr.y.shape[1])])
        i3=np.argmin(abs(tr-3))
        amp=abs(V[-1]-V[i3])
        F=abs((V-V[i3])/(V[-1]-V[i3])) if amp>1e-12 else np.zeros_like(V)
        ids=np.where((tr>=3)&(F>=.632))[0]
        t63=tr[ids[0]]-3 if len(ids) else np.nan
        y=sr.y[:,-1]
        cb,pb=model.avg(y)
        rows.append([k,cb,pb,amp,t63])
        Vs.append(V)
    return pd.DataFrame(rows,columns=["cycle","c_bar","phi_bar","amp","t63_s"]),tr,np.array(Vs)

def ensemble(models,weights):
    dfs=[]; Vs=[]; tr=None
    for m in models:
        d,tr,V=run(m); dfs.append(d); Vs.append(V)
    VV=np.tensordot(weights,np.array(Vs),axes=(0,0))
    i3=np.argmin(abs(tr-3))
    rows=[]
    for k in range(VV.shape[0]):
        V=VV[k]; amp=abs(V[-1]-V[i3])
        F=abs((V-V[i3])/(V[-1]-V[i3])) if amp>1e-12 else np.zeros_like(V)
        ids=np.where((tr>=3)&(F>=.632))[0]
        t63=tr[ids[0]]-3 if len(ids) else np.nan
        cb=np.average([d.loc[k,"c_bar"] for d in dfs],weights=weights)
        pb=np.average([d.loc[k,"phi_bar"] for d in dfs],weights=weights)
        rows.append([k,cb,pb,amp,t63])
    return pd.DataFrame(rows,columns=["cycle","c_bar","phi_bar","amp","t63_s"]),tr,VV

def summarize(df):
    im=int(df["amp"].idxmax())
    peak=df.loc[im,"amp"]
    ids=np.where(df["amp"].values>=peak/2)[0]
    width=df["c_bar"].iloc[ids[-1]]-df["c_bar"].iloc[ids[0]] if len(ids)>1 else 0.0
    return dict(Peak=peak,c_at_peak=df.loc[im,"c_bar"],FWHM_c=width,
                t63_min=df.loc[im,"t63_s"]/60,
                final_phi=df.iloc[-1]["phi_bar"])

if __name__ == "__main__":
    weights=np.array([.1,.2,.4,.2,.1])

    HEO,_,_=run(RadialPF())

    BM_single,_,_=run(RadialPF(
        Ddim=.003,Mphi=.012,W=.50,K=1.60,
        Gmg=0,Bel=.25,ell_relief=.20,Ssurf=.10,ell_wet=.12))

    BM,_,_=ensemble([
        RadialPF(Ddim=.003,Mphi=.012,W=.50,K=1.60,
                 Gmg=0,Bel=.25,ell_relief=.20,Ssurf=s,ell_wet=.12)
        for s in [0,.05,.10,.20,.30]], weights)

    MG,_,_=run(RadialPF(
        Ddim=.0015,Mphi=.001,W=.80,K=1.80,
        Gmg=.35,Bel=.20,ell_relief=.08,Ssurf=.08,ell_wet=.06))

    BMMG,_,_=ensemble([
        RadialPF(Ddim=.003,Mphi=.0008,W=.70,K=1.70,
                 Gmg=.35,Bel=.25,ell_relief=.20,Ssurf=s,ell_wet=.12)
        for s in [0,.10,.20,.30,.40]], weights)

    cases={"HEO":HEO,"BM-HEO":BM,"Mg-HEO":MG,"BM-Mg-HEO":BMMG}
    out=[]
    for name,df in cases.items():
        row={"Sample":name}; row.update(summarize(df)); out.append(row)
    print(pd.DataFrame(out).to_string(index=False))

    # Ablation tests
    MG_stab,_,_=run(RadialPF(Mphi=.015,W=.80,Gmg=.45))
    MG_mob,_,_=run(RadialPF(Mphi=.001,W=.80,Gmg=0))
    print("\nMg ablation")
    for name,df in {"HEO":HEO,"stabilization only":MG_stab,
                    "mobility only":MG_mob,
                    "stabilization + mobility":MG}.items():
        print(name,summarize(df))

    print("\nBM ablation")
    for name,df in {"HEO":HEO,"BM single":BM_single,
                    "BM heterogeneous":BM}.items():
        print(name,summarize(df))
