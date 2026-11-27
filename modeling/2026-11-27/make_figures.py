"""Draw Figure 6 and supplementary figures from the raw-derived CSVs.
Usage: python make_figures.py (from any directory)."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.colors import to_rgb

ROOT=Path(__file__).resolve().parent
D=ROOT/'data'; OUT=ROOT/'figures'; OUT.mkdir(exist_ok=True)
p=pd.read_csv(D/'pulse_metrics.csv'); h=pd.read_csv(D/'halfcycle_capacity.csv')
S=['HEO','BM-HEO','Mg-HEO','BM-Mg-HEO']
# Exact dominant line RGB values sampled from Figure 4 in the author Word (2026-11-11).
C=dict(zip(S,['#244c78','#c76b43','#25836e','#8665a1']))
M=dict(zip(S,['o','s','^','D']))
LS={s:('-' if 'BM' not in s else '--') for s in S}
mpl.rcParams.update({'font.family':'Liberation Sans','font.size':9,'axes.labelsize':9.5,'axes.titlesize':10,'axes.linewidth':0.8,
 'xtick.direction':'out','ytick.direction':'out','xtick.major.size':3,'ytick.major.size':3,'xtick.major.width':0.75,'ytick.major.width':0.75,
 'legend.fontsize':8.6,'legend.frameon':False,'pdf.fonttype':42,'svg.fonttype':'none','savefig.facecolor':'white','figure.facecolor':'white'})
VLAB=r'End-of-rest QOCV (V vs. Li/Li$^+$)'
QLAB=r'Nominal GITT charge (mAh g$^{-1}$)'
TLAB=r'$t_{63}$ (min)'
FRACTION='Cumulative rested-pulse fraction'
def style(ax):
    ax.spines[['top','right']].set_visible(False);ax.tick_params(pad=3)
def panel(ax,label,title=None):
    ax.text(0,1.08,f'({label})',transform=ax.transAxes,ha='left',va='bottom',fontsize=10.5)
    if title:ax.set_title(title,pad=8)
def legend(fig,marker=True):
    handles=[Line2D([0],[0],color=C[s],lw=1.5,ls=LS[s],marker=M[s] if marker else None,ms=4,label=s) for s in S]
    fig.legend(handles=handles,loc='upper center',ncol=4,bbox_to_anchor=(.54,.995),columnspacing=1.6,handlelength=2.3)
def save(fig,name):
    for fmt in ['png','pdf','svg']:
        fig.savefig(OUT/f'{name}.{fmt}',dpi=300)
    plt.close(fig)
def pulse_curve(ax,cycle,kind):
    for s in S:
        a=p[(p['sample']==s)&(p.cycle==cycle)&(p.direction=='delith')].sort_values('pulse')
        y=a.Q_full/a.Q_full.max() if kind=='fraction' else a.t63_since_3s_s/60
        ax.plot(a.QOCV,y,color=C[s],ls=LS[s],lw=1.5,marker=M[s],ms=2.3,markevery=4,mew=.3)
    style(ax);ax.set_xlabel(VLAB);ax.set_xlim(.16,2.24);ax.set_xticks([.25,.5,.75,1,1.25,1.5,1.75,2]);ax.set_ylabel(FRACTION if kind=='fraction' else TLAB)
    if kind=='fraction':ax.set_ylim(0,1.04);ax.set_yticks(np.arange(0,1.01,.2))
    if kind=='t63':ax.set_ylim(0,12);ax.set_yticks(np.arange(0,13,2))
def main():
    # Figure 6: same y scale, same x scale.
    fig,axes=plt.subplots(2,2,figsize=(7.2,5.5))
    fig.subplots_adjust(left=.12,right=.975,bottom=.10,top=.865,wspace=.36,hspace=.43)
    legend(fig)
    for ax,lab,direction,title in zip(axes[0],['a','b'],['lith','delith'],['Lithiation','Delithiation']):
        for s in S:
            a=h[(h['sample']==s)&(h.direction==direction)].sort_values('cycle')
            ax.plot(a.cycle,a.Q_total,color=C[s],ls=LS[s],marker=M[s],lw=1.5,ms=4.8)
        style(ax);panel(ax,lab,title);ax.set_xticks([1,2,3],['C1','C2','C3']);ax.set_xlim(.8,3.2);ax.set_ylim(400,1400);ax.set_yticks(np.arange(400,1401,200));ax.set_ylabel(QLAB)
    for ax,lab,kind,title in zip(axes[1],['c','d'],['fraction','t63'],['C3 delithiation','C3 delithiation']):
        pulse_curve(ax,3,kind);panel(ax,lab,title)
    save(fig,'Figure_6_C1_C3')
    # S4 (supplement for existing R3 text); signed magnitude contributions.
    a=p[(p['sample']=='HEO')&(p.half==1)&(p.pulse.between(26,55))].copy()
    fig,axes=plt.subplots(1,2,figsize=(7.2,2.65));fig.subplots_adjust(left=.10,right=.98,bottom=.19,top=.85,wspace=.34)
    colors=['#8faabd','#bc8a68','#244c78']; cols=['W3_60_mV','W60_600_mV','W600_3600_mV']; names=['3–60 s','60–600 s','600–3600 s']
    ax=axes[0];ax.stackplot(a.pulse,*[a[c] for c in cols],labels=names,colors=colors,alpha=.93)
    ax.plot(a.pulse,a.A_mV,color='#26333e',lw=1.25);ax.axvline(50,color='#444',lw=.75,ls=':');ax.set_xlim(26,55);ax.set_ylim(0,220);ax.set_xlabel('First-lithiation pulse index');ax.set_ylabel(r'$\Delta E_{\mathrm{rest}}$ (mV)');ax.legend(loc='upper left',fontsize=7.7,frameon=True,facecolor='white',framealpha=.9,edgecolor='none');panel(ax,'a','HEO, R3');style(ax)
    ax=axes[1];r=a.set_index('pulse');diff=r.loc[50,cols]-r.loc[26,cols]
    bars=ax.bar(range(3),diff,color=colors,width=.66);ax.axhline(0,color='#444',lw=.8);ax.set_xticks(range(3),names);ax.set_ylabel('Change in recovery (mV)');ax.set_ylim(-18,48)
    for i,v in enumerate(diff):ax.text(i,v+(1.5 if v>=0 else -1.5),f'{v:+.1f}',ha='center',va='bottom' if v>=0 else 'top',fontsize=9)
    panel(ax,'b','Pulse 50 minus pulse 26');style(ax);save(fig,'SI_R3_recovery_windows')
    # Full C1-C3 lithiation / delithiation trajectories, per sample.
    for direction,letter in [('lith','Lithiation'),('delith','Delithiation')]:
        fig,axs=plt.subplots(4,3,figsize=(7.2,8.0),sharex=True,sharey='col');fig.subplots_adjust(left=.11,right=.985,bottom=.075,top=.90,wspace=.30,hspace=.39)
        hs=[Line2D([0],[0],color='#404040',alpha=a,lw=1.4,ls=ls,label=f'C{i}') for i,(a,ls) in enumerate([(0.37,':'),(.65,'--'),(1,'-')],1)]
        fig.legend(handles=hs,loc='upper center',ncol=3,bbox_to_anchor=(.56,.993),handlelength=2.3)
        for j,name in enumerate(['QOCV',r'$\Delta E_{\mathrm{rest}}$',r'$t_{63}$']):axs[0,j].set_title(name,pad=8)
        for i,s in enumerate(S):
            for cyc,alpha,ls in [(1,.40,':'),(2,.68,'--'),(3,1,'-')]:
                r=p[(p['sample']==s)&(p.direction==direction)&(p.cycle==cyc)].sort_values('pulse');x=r.Q_full/r.Q_full.max()
                for j,y in enumerate([r.QOCV,r.A_mV,r.t63_since_3s_s/60]):
                    axs[i,j].plot(x,y,c=C[s],alpha=alpha,ls=ls,lw=1.4)
            for j,ax in enumerate(axs[i]):
                style(ax);ax.set_xlim(0,1.02)
                if i==0:ax.text(0,1.12,f'({chr(97+j)})',transform=ax.transAxes,fontsize=10)
                if i==3:ax.set_xlabel('Rested-pulse fraction')
            axs[i,0].set_ylabel(f'{s}\nQOCV (V)',color=C[s]);axs[i,1].set_ylabel('mV');axs[i,2].set_ylabel('min')
        save(fig,f'SI_C1_C3_{letter}_profiles')
    # C2 complement to the C3 panels
    fig,axes=plt.subplots(1,2,figsize=(7.2,2.9));fig.subplots_adjust(left=.12,right=.975,bottom=.19,top=.76,wspace=.36);legend(fig)
    for ax,lab,kind in zip(axes,['a','b'],['fraction','t63']):
        pulse_curve(ax,2,kind);panel(ax,lab,'C2 delithiation')
    save(fig,'SI_C2_delithiation')
    # Existing conditional C2→C3 model predictions from the archived comparison.
    f=D/'capacity_shape_C3_predictions.csv'
    if f.exists():
        m=pd.read_csv(f);fig,axes=plt.subplots(1,2,figsize=(7.2,2.95));fig.subplots_adjust(left=.12,right=.975,bottom=.18,top=.84,wspace=.35)
        for ax,lab,contrast,title in zip(axes,['a','b'],['BM (no Mg)','BM (with Mg)'],['BM vs HEO','BM-Mg vs Mg']):
            r=m[(m.contrast==contrast)&(m.direction=='delith')]
            a=r[r.model=='C1_shift']
            if a.empty:continue
            ax.axhline(0,c='.4',lw=.8)
            for model,name,c,ls in [('C1_shift','Shift only','#686868','--'),('C2_population','Shift + redistribution','#244c78','-')]:
                rr=r[r.model==model]
                ax.plot(rr.QOCV,rr.predicted_C3-rr.observed_C3,c=c,ls=ls,lw=1.5,label=name)
            style(ax);panel(ax,lab,title);ax.set_xlabel(VLAB);ax.set_ylabel('Predicted − measured fraction');ax.set_ylim(-.04,.04);ax.legend(loc='lower left',fontsize=7.5)
        save(fig,'SI_C2_to_C3_charge_model_residuals')

    # Former conceptual main Figure 6, recast as a supplemental, explicitly non-causal guide.
    a=p[(p['sample']=='HEO')&(p.half==1)].sort_values('pulse')
    fig=plt.figure(figsize=(7.2,4.2))
    ax=fig.add_axes([.105,.43,.86,.46]);style(ax)
    bounds=np.array([0,6,25,55,65])*100*600/3600
    for j,(lo,hi) in enumerate(zip(bounds[:-1],bounds[1:])):
        ax.axvspan(lo,hi,color=['#e4edf3','#e4edf3','#f4ede3','#e5f1ed'][j],zorder=0)
        if j>0:ax.axvline(lo,color='#7795aa',lw=.9,ls='--')
        ax.text((lo+hi)/2,1.60,f'R{j+1}',ha='center',va='center',color='#27455e',fontsize=10)
    ax.plot(a.Q_full,a.QOCV,c=C['HEO'],lw=1.6)
    ax.set_xlim(0,1100);ax.set_ylim(0,1.72);ax.set_ylabel(r'QOCV (V vs. Li/Li$^+$)');ax.set_xlabel(QLAB)
    fig.text(.535,.95,'Measured HEO first-lithiation trajectory',ha='center',fontsize=10)
    fig.text(.105,.244,'Literature-guided context (overlapping processes; not phase assignments)',weight='bold',fontsize=9)
    context=[('R1','Early Li uptake;\noxide rearrangement'),('R2','Oxide reconstruction;\nearly reduction'),('R3','Further reduction;\nmetal/Li₂O development'),('R4','Residual reduction;\npossible interfacial effects')]
    for j,(r,t) in enumerate(context):
        x=.105+j*.218
        fig.text(x,.186,r,color='#244c78',fontsize=9.2,weight='bold')
        fig.text(x,.145,t,fontsize=8.2,va='top',linespacing=1.3)
    save(fig,'SI_Operational_regions_context')

if __name__=="__main__":main()
