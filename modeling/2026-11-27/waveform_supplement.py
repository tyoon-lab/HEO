"""Reproduce the archived Nov 20 conditional normalized-waveform test.
Run after recompute_pulse_metrics.py. For fast rerun, supply verified NPZ arrays
(--npz-dir) or use raw XLSX directly (--raw-dir). The waveform-grid CSV is also
saved so the figure and scores can be regenerated without the original workbooks.
"""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from recompute_pulse_metrics import FILES, read_xlsx
from make_figures import C,LS,style,panel,save,VLAB
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent; D=ROOT/'data'
T=np.array([10,20,30,45,60,90,120,180,240,300,450,600,900,1200,1500,1800,2400,3000,3500.])
def load_raw(raw_dir,npz_dir):
    rows=[]
    for sample,filename in FILES.items():
        if npz_dir:
            z=np.load(npz_dir/f'raw_{Path(filename).stem}.npz');idx,t,v,i=[z[k] for k in ['index','t','v','i']]
        else:idx,t,v,i=read_xlsx(raw_dir/filename)
        valid=np.isfinite(t)&np.isfinite(v)&(abs(i)<.01)&(idx>0);t,v,i=[q[valid] for q in [t,v,i]]
        cad=np.median(np.diff(t));sg=np.sign(np.round(i,6))
        st=np.r_[0,np.flatnonzero(sg[1:]!=sg[:-1])+1];en=np.r_[st[1:],len(sg)]
        half=0;prev=0;n=0
        for k,(a,b) in enumerate(zip(st,en)):
            pol=sg[a]
            if not pol:continue
            if pol!=prev:half+=1;prev=pol;n=0
            if half>6:break
            if abs(t[b-1]-t[a]+cad-600)>.011 or k+1>=len(st) or sg[st[k+1]]!=0:continue
            aa,bb=st[k+1],en[k+1];tr=t[aa:bb]-t[b-1];vr=v[aa:bb]
            if tr[0]>3.011 or tr[-1]<3599.989:continue
            n+=1;E=np.interp(T,tr,vr);F=(E-E[0])/(E[-1]-E[0])
            rows.append(dict(sample=sample,cycle=(half+1)//2,direction='lith' if pol<0 else 'delith',pulse=n,QOCV=vr[-1],A_10_3500_V=abs(E[-1]-E[0]),**{f'F_{int(ti)}s':fi for ti,fi in zip(T,F)}))
    return pd.DataFrame(rows)
def pack(z,s,cyc):
    x=z[(z['sample']==s)&(z.cycle==cyc)&(z.direction=='delith')].sort_values('pulse')
    return (x.QOCV.to_numpy(),(x.pulse.to_numpy()-.5)/len(x),x[[f'F_{int(ti)}s' for ti in T]].to_numpy())
def prep(r,t,delta):
    vr,ur,fr=r;vt,ut,ft=t
    o=np.argsort(vr)
    q=(vt>=.5)&(vt<=1.7)&(vt-delta>min(vr)+.05)&(vt-delta<max(vr)-.05)
    return np.column_stack([np.interp(vt[q]-delta,vr[o],fr[o,j]) for j in range(len(T))]),ft[q],vt[q]
def warp(F,lam):
    a=np.array([np.interp(10+(T-10)/lam,T,row) for row in F]); return (a-a[:,[0]])/(a[:,[-1]]-a[:,[0]])
def curv(F,c):return F+c*F*(1-F)
def rms(x):return np.sqrt(np.mean(x*x))
def fit_pair(z,ref,treat):
    r2,t2=pack(z,ref,2),pack(z,treat,2);q=np.linspace(.12,.88,60)
    delta=np.median(np.interp(q,t2[1],t2[0])-np.interp(q,r2[1],r2[0]))
    f2,g2,_=prep(r2,t2,delta)
    a=f2*(1-f2);c=np.clip(np.sum((g2-f2)*a)/np.sum(a*a),-.9,.9)
    lam=np.exp(minimize_scalar(lambda l:rms(warp(f2,np.exp(l))-g2),bounds=(np.log(.45),np.log(2.3)),method='bounded',options={'xatol':1e-5}).x)
    r3,t3=pack(z,ref,3),pack(z,treat,3);f3,g3,V=prep(r3,t3,delta)
    models={'Unchanged reference':f3,'Voltage curvature':curv(f3,c),'Time stretch':warp(f3,lam)}
    rec=[dict(reference=ref,treatment=treat,n_pulses=len(V),C2_offset_V=delta,C2_curvature=c,C2_time_factor=lam,model=k,C3_RMSE=rms(pred-g3),C3_F300_treat_minus_ref_pp=100*np.mean(g3[:,9]-f3[:,9])) for k,pred in models.items()]
    return f3,g3,models,rec
def main():
    a=argparse.ArgumentParser();a.add_argument('--raw-dir',type=Path);a.add_argument('--npz-dir',type=Path);args=a.parse_args()
    if args.raw_dir or args.npz_dir:
        z=load_raw(args.raw_dir,args.npz_dir);z.to_csv(D/'waveform_grid_10_3500s.csv',index=False,float_format='%.12g')
    else:z=pd.read_csv(D/'waveform_grid_10_3500s.csv')
    assert len(z)==1020
    rec=[];fig,axes=plt.subplots(2,2,figsize=(7.2,5.5));fig.subplots_adjust(left=.11,right=.98,bottom=.105,top=.91,hspace=.42,wspace=.38)
    for j,(ref,treat) in enumerate([('HEO','BM-HEO'),('Mg-HEO','BM-Mg-HEO')]):
        f,g,models,rr=fit_pair(z,ref,treat);rec.extend(rr)
        ax=axes[0,j];ax.plot(T,np.mean(f,axis=0),color=C[ref],ls=LS[ref],lw=1.5,label=ref+' (aligned)');ax.plot(T,np.mean(g,axis=0),color=C[treat],ls=LS[treat],lw=1.5,label=treat)
        ax.axvline(300,c='.6',ls=':',lw=.8);ax.set_ylim(0,1.04);ax.set_ylabel('Mean normalized recovery');ax.legend(fontsize=7.7,loc='lower right');panel(ax,'ab'[j],f'C3: {treat} / {ref}')
        ax=axes[1,j];colors={'Unchanged reference':'#777777','Voltage curvature':'#244c78','Time stretch':'#c76b43'}
        for k,pred in models.items():
            ax.plot(T,100*np.mean(pred-g,axis=0),color=colors[k],ls='--' if k=='Time stretch' else '-',lw=1.5,label=k)
        ax.axhline(0,c='.35',lw=.7);ax.set_ylim(-1,4.5);ax.set_ylabel('Mean signed residual (pp)');ax.legend(fontsize=7.5,loc='upper right');panel(ax,'cd'[j],'C2-calibrated shape test')
        for ax in axes[:,j]:
            style(ax);ax.set_xscale('log');ax.set_xlim(10,3500);ax.set_xticks([10,100,1000],['10','100','1000']);ax.set_xlabel('Rest time (s)')
    save(fig,'SI_C2_to_C3_waveform_shape')
    df=pd.DataFrame(rec);df.to_csv(D/'waveform_recomputed_scores.csv',index=False,float_format='%.12g');print(df.to_string(index=False))
if __name__=='__main__':main()
