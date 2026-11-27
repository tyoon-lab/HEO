"""Rebuild finite-rest GITT metrics from the four original .xlsx workbooks.
Usage: python recompute_pulse_metrics.py --raw-dir path --out-dir path
Place the source files under the four names specified in FILES. Python 3, NumPy, pandas.
Raw XLSX XML access avoids Excel row-limit truncation and loads both data sheets.
"""
import argparse, re, zipfile, hashlib
from pathlib import Path
import numpy as np
import pandas as pd

FILES={'HEO':'HEO.xlsx','BM-HEO':'BM.xlsx','Mg-HEO':'Mg.xlsx','BM-Mg-HEO':'BM_Mg.xlsx'}
V_RE=re.compile(rb'<(?:x:)?v>([^<]*)</(?:x:)?v>')
ROW_RE=re.compile(rb'<(?:x:)?row\b[^>]*>(.*?)</(?:x:)?row>',re.S)
SST_RE=re.compile(rb'<(?:x:)?si><(?:x:)?t>([^<]*)</(?:x:)?t></(?:x:)?si>')
def parse_time(b):
    try:
        d,h,m,s=b.decode().split(':')
        return int(d)*86400+int(h)*3600+int(m)*60+float(s)
    except (ValueError,UnicodeDecodeError): return np.nan

def read_xlsx(path):
    A=[]
    with zipfile.ZipFile(path) as z:
        sst=None
        if 'xl/sharedStrings.xml' in z.namelist():
            sst=np.fromiter((parse_time(m.group(1)) for m in SST_RE.finditer(z.read('xl/sharedStrings.xml'))),dtype=float)
        for sheet in sorted(n for n in z.namelist() if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',n) and not n.endswith('/sheet1.xml')):
            b=z.read(sheet)
            rows=[]
            for m in ROW_RE.finditer(b):
                a=V_RE.findall(m.group(1))
                if len(a)<4: continue
                try:
                    idx=int(a[0]); t=sst[int(a[1])] if sst is not None else parse_time(a[1])
                    v=float(a[2]); i=float(a[3])
                except (IndexError,ValueError,OverflowError): continue
                if idx>0 and np.isfinite(t) and np.isfinite(v) and abs(i)<0.01:
                    rows.append((idx,t,v,i))
            A.append(np.asarray(rows,dtype=float))
            print(path.name,sheet,len(rows),flush=True)
    a=np.concatenate(A)
    # Duplicates must agree in all four fields; no silently discarded disagreement.
    _,first,counts=np.unique(a[:,0],return_index=True,return_counts=True)
    if np.any(counts>1):
        for i in a[first[counts>1],0]:
            d=a[a[:,0]==i]
            assert np.allclose(d,d[0],rtol=0,atol=1e-9),f'conflicting index {i}'
    a=a[np.sort(first)]
    assert np.all(np.diff(a[:,0])==1) and np.all(np.diff(a[:,1])>0),path
    return a.T

def first_cross(t,v,endpoint=3600):
    e3=np.interp(3,t,v); eend=np.interp(endpoint,t,v)
    d=eend-e3
    if abs(d)<1e-4: return np.nan
    xx=t[(t>3)&(t<endpoint)]; ts=np.r_[3,xx,endpoint]
    ff=(np.interp(ts,t,v)-e3)/d
    idx=np.flatnonzero(ff>=1-np.exp(-1))
    if not len(idx):return np.nan
    k=idx[0]
    return ts[k-1]+(ts[k]-ts[k-1])*(1-np.exp(-1)-ff[k-1])/(ff[k]-ff[k-1])

def extract(sample,idx,t,v,i):
    ok=np.isfinite(t)&np.isfinite(v)&(abs(i)<.01)&(idx>0)
    idx,t,v,i=[x[ok] for x in [idx,t,v,i]]
    assert np.all(np.diff(idx)==1) and np.all(np.diff(t)>0),sample
    cad=float(np.median(np.diff(t))); sg=np.sign(np.round(i,6))
    st=np.r_[0,np.flatnonzero(sg[1:]!=sg[:-1])+1]; en=np.r_[st[1:],len(sg)]
    half=0;prev=0;h={};p=[];protocol=[]
    for k,(a,b) in enumerate(zip(st,en)):
        sign=sg[a]
        if sign==0:continue
        if sign!=prev:half+=1;prev=sign
        if half>6: break
        d=t[b-1]-t[a]+cad
        key={'sample':sample,'half':half,'cycle':(half+1)//2,'direction':'lith' if sign<0 else 'delith'}
        item=h.setdefault(half,dict(key, n_full=0,pulse_count=0,Q_total=0))
        item['pulse_count']+=1;item['Q_total']+=100*d/3600
        rest_t=0.;has_rest=False
        if k+1<len(st) and sg[st[k+1]]==0:
            aa,bb=st[k+1],en[k+1]; tr=t[aa:bb]-t[b-1];vr=v[aa:bb];rest_t=tr[-1];has_rest=True
        # 0.01 s rounding tolerance for timestamp arithmetic. Exact protocol window.
        complete=bool(abs(d-600)<=0.011 and has_rest and tr[0]<=3.011 and tr[-1]>=3599.989)
        protocol.append(dict(key,pulse_including_terminal=item['pulse_count'],start_s=t[a],pulse_duration_s=d,rest_end_s=rest_t,complete_rest=complete))
        if not complete:continue
        item['n_full']+=1
        pulse=item['n_full']
        e3,e10,e60,e300,e600,e1200,e3500,e3600=np.interp([3,10,60,300,600,1200,3500,3600],tr,vr)
        recovery=e3600-e3
        ts=first_cross(tr,vr)
        # Reproduce archived model metric on exact 3,10,...,3500 s grid.
        tg=np.r_[3,np.arange(10,3501,10)];vg=np.interp(tg,tr,vr);f=(vg-vg[0])/(vg[-1]-vg[0]);ix=np.flatnonzero(f>=1-np.exp(-1))[0]
        t_old=tg[ix-1]+(tg[ix]-tg[ix-1])*(1-np.exp(-1)-f[ix-1])/(f[ix]-f[ix-1])
        sign_recovery=np.sign(recovery)
        p.append(dict(key,pulse=pulse,Q_full=pulse*100*600/3600,QOCV=float(vr[-1]),QOCV3600=e3600,E3=e3,E10=e10,E60=e60,E300=e300,E600=e600,E1200=e1200,E3500=e3500,E3600=e3600,A_mV=abs(recovery)*1000,t63_s=ts,t63_since_3s_s=ts-3,
                      A3500_mV=abs(e3500-e3)*1000,t63_3500_archived_s=t_old,F300_10_3500=(e300-e10)/(e3500-e10),F300_3_3500=(e300-e3)/(e3500-e3),
                      W3_60_mV=(e60-e3)*1000*sign_recovery,W60_600_mV=(e600-e60)*1000*sign_recovery,W600_3600_mV=(e3600-e600)*1000*sign_recovery))
    assert len(h)==6
    return p,list(h.values()),protocol,{'sample':sample,'rows':len(t),'cadence_s':cad,'first_index':idx[0],'last_index':idx[-1]}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--raw-dir',type=Path,required=True); parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--npz-dir',type=Path,help='Optional interim arrays with filenames raw_<stem>.npz (from same raw workbooks)')
    args=parser.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True)
    p=[];h=[];u=[];a=[]
    for sample,filename in FILES.items():
        path=args.raw_dir/filename
        if args.npz_dir:
            z=np.load(args.npz_dir/f'raw_{path.stem}.npz'); data=[z[c] for c in ['index','t','v','i']]
        else: data=read_xlsx(path)
        pp,hh,uu,aa=extract(sample,*data)
        aa.update(filename=filename,sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        p+=pp; h+=hh;u+=uu;a.append(aa);print(sample,len(pp),flush=True)
    for name,records in [('pulse_metrics',p),('halfcycle_capacity',h),('pulse_selection',u),('source_manifest',a)]:
        pd.DataFrame(records).to_csv(args.out_dir/f'{name}.csv',index=False,float_format='%.10g')

if __name__=='__main__':main()
