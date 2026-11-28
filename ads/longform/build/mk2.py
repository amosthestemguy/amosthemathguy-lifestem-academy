import json,subprocess,sys,urllib.parse as U
cfg=json.load(open(sys.argv[1]))
src=cfg['src'];SEGS=cfg['segs'];out=cfg['out']
FIX={'dirty':'thirty',**cfg.get('fix',{})}
REPL=cfg.get('repl',{})
W=[w for x in json.load(open(src.replace('.mp4','.json'))) for w in x['words']]
def tt(t): h=int(t//3600);m=int(t%3600//60);s=t%60;return f"{h}:{m:02d}:{s:05.2f}"
def rp(t):
    for k,v in REPL.items(): t=t.replace(k,v)
    return t
ev=[];off=0
for a,b in SEGS:
    ws=[w for w in W if a<=w['s'] and w['e']<=b+0.2];cur=[]
    def flush():
        if cur: ev.append((cur[0]['s']-a+off,cur[-1]['e']-a+off,rp(' '.join(FIX.get(w['w'].strip(),w['w'].strip()) for w in cur))))
    for w in ws:
        if cur and (len(cur)>=7 or w['s']-cur[-1]['e']>0.8 or cur[-1]['w'].strip()[-1:] in '.?!'): flush();cur=[]
        cur.append(w)
    flush(); off+=b-a
ev=[(s,min(e,ev[i+1][0]) if i+1<len(ev) else e,t) for i,(s,e,t) in enumerate(ev)]
hdr=open('cap.ass').read().split('[Events]')[0]+"[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
ass=out.replace('.mp4','.ass')
open(ass,'w').write(hdr+'\n'.join(f"Dialogue: 0,{tt(s)},{tt(e)},Cap,,0,0,0,,{t}" for s,e,t in ev)+'\n')
q=lambda d:'&'.join(f"{k}={U.quote(v)}" for k,v in d.items())
base={'chan':cfg['chan'],'kind':cfg['kind']}
fr,en=out.replace('.mp4','_frame.png'),out.replace('.mp4','_end.png')
subprocess.run(['node','shot.js',json.dumps([[q({**base,'mode':'frame','title':cfg['title']}),fr],[q({**base,'mode':'end','sub':cfg['sub']}),en]])],check=True)
print(out,'main',round(off,1))
fc=[];ins=[]
for i,(a,b) in enumerate(SEGS):
    ins+=['-ss',str(a),'-t',str(b-a),'-i',src];d=b-a
    crop=(cfg["crop"]+",") if cfg.get("crop") else ""
    fc.append(f"[{i}:v]{crop}setpts=PTS-STARTPTS,fps=30[v{i}];[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.12,afade=t=out:st={d-0.15}:d=0.15[a{i}]")
n=len(SEGS)
fc.append(''.join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[cv][ca]")
fc.append(f"color={cfg.get('bg','white')}:s=1920x1080:r=30:d={off}[bg];[cv]scale=1804:730:force_original_aspect_ratio=decrease,setsar=1[sv];[bg][sv]overlay=(W-w)/2:110+(730-h)/2:shortest=1[b1];[b1][{n}:v]overlay[b2];[b2]ass={ass},format=yuv420p[vmain]")
fc.append(f"[{n+1}:v]fps=30,format=yuv420p,fade=t=in:d=0.4[vend];anullsrc=r=48000:cl=mono,atrim=0:8[aend];[ca]aresample=48000,loudnorm=I=-16:TP=-1.5[an]")
fc.append("[vmain][an][vend][aend]concat=n=2:v=1:a=1[v][a]")
subprocess.run(['ffmpeg','-v','error','-y']+ins+['-i',fr,'-loop','1','-t','8','-i',en,'-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','21','-c:a','aac','-b:a','160k','-movflags','+faststart',out],check=True)
