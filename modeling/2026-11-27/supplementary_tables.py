"""Generate SI charge accounting and direct validation/sensitivity tables from fresh pulse metrics."""
from pathlib import Path
from itertools import product
import pandas as pd
import numpy as np
from scipy.interpolate import PchipInterpolator
ROOT=Path(__file__).resolve().parent;D=ROOT/'data'
p=pd.read_csv(D/'pulse_metrics.csv');h=pd.read_csv(D/'halfcycle_capacity.csv')
S=['HEO','BM-HEO','Mg-HEO','BM-Mg-HEO']
P=[('BM/no Mg','HEO','BM-HEO'),('BM/with Mg','Mg-HEO','BM-Mg-HEO'),('Mg/no BM','HEO','Mg-HEO'),('Mg/with BM','BM-HEO','BM-Mg-HEO')]
L=dict(zip(S,[(6,25,55),(9,38,60),(7,24,42),(9,35,46)]))
N={s:len(p[(p['sample']==s)&(p.half==1)]) for s in S}
Q=100*600/3600
def rcounts(s,shift=(0,0,0)):
    return np.diff(np.r_[0,np.array(L[s])+shift,N[s]])
rows=[]
for s in S:
    q=rcounts(s)
    rows.append(dict(sample=s,n_complete=N[s],L1=L[s][0],L3=L[s][1],L4=L[s][2],**{f'R{i+1}_pulses':n for i,n in enumerate(q)},**{f'R{i+1}_mAh_g':n*Q for i,n in enumerate(q)},**{f'R{i+1}_share_pct':100*n/N[s] for i,n in enumerate(q)}))
pd.DataFrame(rows).to_csv(D/'Table_S1_region_charge.csv',index=False)
d=[];sens=[]
for label,r,t in P:
    x=(rcounts(t)-rcounts(r))*Q
    d.append(dict(contrast=label,**{f'R{i+1}_delta_mAh_g':v for i,v in enumerate(x)},net_delta_mAh_g=x.sum()))
    arr=np.array([(rcounts(t,np.array(s[3:]))-rcounts(r,np.array(s[:3])))*Q for s in product([-1,0,1],repeat=6)])
    for i in range(4):
        sens.append(dict(contrast=label,region=f'R{i+1}',nominal=x[i],min=arr[:,i].min(),max=arr[:,i].max(),n_positive=np.sum(arr[:,i]>1e-8),n_negative=np.sum(arr[:,i]<-1e-8),n_zero=np.sum(abs(arr[:,i])<1e-8),scenarios=729))
    # For Mg contrasts, count scenarios in which R3 is largest absolute loss within the specified pair.
    strict=np.all(arr[:,2,None]<np.delete(arr,2,axis=1),axis=1)
    weak=np.all(arr[:,2,None]<=np.delete(arr,2,axis=1),axis=1)
    print(label,'R3 strict largest loss',sum(strict),'ties',sum(weak)-sum(strict))
pd.DataFrame(d).to_csv(D/'Table_S2_region_contrasts.csv',index=False)
pd.DataFrame(sens).to_csv(D/'Table_S3_region_boundary_sensitivity.csv',index=False)
# S4: onset, peak amplitude, end, and pristine pulse 50.
rr=[]
for s in S:
    a=p[(p['sample']==s)&(p.half==1)&(p.pulse>L[s][1])&(p.pulse<=L[s][2])]
    for state,row in [('R3 onset',a.iloc[0]),('R3 maximum',a.loc[a.A_mV.idxmax()]),('R3 end',a.iloc[-1])]:
        rr.append({'sample':s,'state':state,**row[['pulse','QOCV','A_mV','W3_60_mV','W60_600_mV','W600_3600_mV','t63_since_3s_s']].to_dict()})
pd.DataFrame(rr).to_csv(D/'Table_S4_R3_recovery.csv',index=False)
# S5: common QOCV interpolation of window amplitudes, centered finite slope in adjacent pulses.
r=[]
for s in S:
    a=p[(p['sample']==s)&(p.half==1)].sort_values('pulse')
    slope=np.abs(np.gradient(a.QOCV,a.Q_full))*1000
    for V in [.48,.50]:
        row=dict(sample=s,QOCV=V,abs_QOCV_slope_mV_per_mAh_g=np.interp(V,a.QOCV[::-1],slope[::-1]))
        for col in ['A_mV','W3_60_mV','W60_600_mV','W600_3600_mV']:
            row[col]=np.interp(V,a.QOCV[::-1],a[col][::-1])
        r.append(row)
pd.DataFrame(r).to_csv(D/'Table_S5_common_QOCV_recovery.csv',index=False)
# New S7: whole-half-cycle charge (24 rows) is data/halfcycle_capacity.csv.
# New S8: voltage window normalized charge. Both denominator conventions retained.
rows=[]
for cy in [2,3]:
    for s in S:
        a=p[(p['sample']==s)&(p.cycle==cy)&(p.direction=='delith')].sort_values('QOCV')
        q=PchipInterpolator(a.QOCV,a.Q_full,extrapolate=False)([1.05,1.40,1.70])
        n=a.Q_full.max();total=h[(h['sample']==s)&(h.cycle==cy)&(h.direction=='delith')].Q_total.iloc[0]
        for lo,hi,qw in zip([1.05,1.40],[1.40,1.70],np.diff(q)):
            rows.append(dict(sample=s,cycle=cy,Vlo=lo,Vhi=hi,Q_window_mAh_g=qw,Q_rested_total=n,Q_halfcycle_total=total,rested_pct=100*qw/n,halfcycle_pct=100*qw/total))
pd.DataFrame(rows).to_csv(D/'Table_S8_delithiation_voltage_windows.csv',index=False)
# Direct potential-matched t63 contrasts using the archived C2-calibrated shift.
# Three-second subtraction cancels between samples, but the end window matters.
mod=pd.read_csv(D/'kinetic_model_scores.csv');qq=[]
for contrast,ref,treat in [('BM (no Mg)','HEO','BM-HEO'),('BM (with Mg)','Mg-HEO','BM-Mg-HEO')]:
    delta=mod[(mod.contrast==contrast)&(mod.direction=='delith')&(mod.observable=='t63_s')&(mod.model=='K0_potential_only')].deltaV_C2.iloc[0]
    V=np.linspace(.35,1.65,100)
    for col in ['t63_since_3s_s','t63_3500_archived_s']:
        ys=[]
        for s,xx in [(ref,V-delta),(treat,V)]:
            a=p[(p['sample']==s)&(p.cycle==3)&(p.direction=='delith')].sort_values('QOCV');ys.append(PchipInterpolator(a.QOCV,a[col],extrapolate=False)(xx))
        dif=ys[1]-ys[0]
        qq.append(dict(contrast=contrast,reference=ref,treatment=treat,metric=col,C2_shift_V=delta,QOCV_min=V.min(),QOCV_max=V.max(),grid_n=np.isfinite(dif).sum(),mean_treatment_minus_reference_s=np.nanmean(dif)))
pd.DataFrame(qq).to_csv(D/'Table_S10_potential_matched_t63.csv',index=False)
