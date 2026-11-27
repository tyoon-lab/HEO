"""Reproduce the Nov 18 C2→C3 charge-shape gate under both charge denominators.
The shift and redistribution kernels are identical to the previously archived analysis.
No new fitted physical mechanism is introduced.
"""
from pathlib import Path
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from scipy.interpolate import PchipInterpolator
from scipy.special import ndtr
ROOT=Path(__file__).resolve().parent;D=ROOT/'data'
p=pd.read_csv(D/'pulse_metrics.csv');h=pd.read_csv(D/'halfcycle_capacity.csv')
P=[('BM (no Mg)','HEO','BM-HEO'),('BM (with Mg)','Mg-HEO','BM-Mg-HEO'),('Mg (no BM)','HEO','Mg-HEO'),('Mg (with BM)','BM-HEO','BM-Mg-HEO')]
v=np.linspace(.35,1.65,100);phi=ndtr((v-1.18)/.13)-ndtr((v-1.56)/.13)
def curve(s,cy,den):
    a=p[(p['sample']==s)&(p.cycle==cy)&(p.direction=='delith')].sort_values('QOCV')
    tot=h[(h['sample']==s)&(h.cycle==cy)&(h.direction=='delith')].Q_total.iloc[0] if den=='whole_halfcycle' else a.Q_full.max()
    return PchipInterpolator(a.QOCV,a.Q_full/tot,extrapolate=False)
rec=[]
for den in ['whole_halfcycle','fully_rested_pulses']:
    for label,r,t in P:
        rf2,rf3=[curve(r,cy,den) for cy in [2,3]];y2,y3=[curve(t,cy,den)(v) for cy in [2,3]]
        for model in ['shift_only','shift_plus_redistribution']:
            def pred(ref,a):return ref(v-a[0])+(a[1]*phi if len(a)>1 else 0.)
            def residual(a):
                z=pred(rf2,a);ok=np.isfinite(z)&np.isfinite(y2)
                if sum(ok)<55:return np.ones(len(v)+1)*10
                er=np.nan_to_num(z-y2,nan=0.);er[~ok]=.2;return er
            if model=='shift_only':a=least_squares(residual,[0],bounds=([-.2],[.2]),max_nfev=150).x
            else:a=least_squares(residual,[0,0],bounds=([-.2,-.35],[.2,.35]),max_nfev=150).x
            zz=pred(rf3,a);ok=np.isfinite(zz)&np.isfinite(y3)
            rec.append(dict(denominator=den,contrast=label,model=model,C2_shift_V=a[0],C2_redistribution=a[1] if len(a)>1 else 0.,C3_RMSE=np.sqrt(np.mean((zz[ok]-y3[ok])**2)),C3_grid_n=sum(ok)))
df=pd.DataFrame(rec);df.to_csv(D/'Table_S9_charge_model_denominator_sensitivity.csv',index=False,float_format='%.12g')
print(df.to_string(index=False))
