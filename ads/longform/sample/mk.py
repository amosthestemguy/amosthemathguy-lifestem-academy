import json,subprocess,sys
SEGS=[(734.5,819.5),(1062.2,1123.2),(1158.0,1263.5),(1275.5,1326.1)]
FIX={'dirty':'thirty'}
W=[w for x in json.load(open('../proxy/s011.json')) for w in x['words']]
def tt(t): h=int(t//3600);m=int(t%3600//60);s=t%60;return f"{h}:{m:02d}:{s:05.2f}"
ev=[];off=0
for a,b in SEGS:
    ws=[w for w in W if a<=w['s'] and w['e']<=b+0.2]
    cur=[]
    def flush():
        if cur: ev.append((cur[0]['s']-a+off,cur[-1]['e']-a+off,' '.join(FIX.get(w['w'].strip(),w['w'].strip()) for w in cur)))
    for w in ws:
        if cur and (len(cur)>=7 or w['s']-cur[-1]['e']>0.8 or cur[-1]['w'].strip()[-1:] in '.?!'): flush();cur=[]
        cur.append(w)
    flush(); off+=b-a
ev=[(s,min(e,ev[i+1][0]) if i+1<len(ev) else e,t) for i,(s,e,t) in enumerate(ev)]
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,46,&H00FFFFFF,&H00FFFFFF,&H18702408,&H00000000,1,0,0,0,100,100,0,0,3,14,0,2,200,200,236,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open('cap.ass','w').write(hdr+'\n'.join(f"Dialogue: 0,{tt(s)},{tt(e)},Cap,,0,0,0,,{t}" for s,e,t in ev)+'\n')
print('total',off)
fc=[];ins=[]
for i,(a,b) in enumerate(SEGS):
    ins+=['-ss',str(a),'-t',str(b-a),'-i','../proxy/s011.mp4']
    d=b-a
    fc.append(f"[{i}:v]setpts=PTS-STARTPTS,fps=30[v{i}];[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.12,afade=t=out:st={d-0.15}:d=0.15[a{i}]")
n=len(SEGS)
fc.append(''.join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[cv][ca]")
fc.append(f"color=white:s=1920x1080:r=30:d={off}[bg];[cv]scale=1804:730[sv];[bg][sv]overlay=58:110:shortest=1[b1];[b1][{n}:v]overlay[b2];[b2]ass=cap.ass,format=yuv420p[vmain]")
fc.append(f"[{n+1}:v]fps=30,format=yuv420p,fade=t=in:d=0.4[vend];anullsrc=r=48000:cl=mono,atrim=0:8[aend];[ca]aresample=48000,loudnorm=I=-16:TP=-1.5[an]")
fc.append("[vmain][an][vend][aend]concat=n=2:v=1:a=1[v][a]")
cmd=['ffmpeg','-v','error','-y']+ins+['-i','frame.png','-loop','1','-t','8','-i','end.png','-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','21','-c:a','aac','-b:a','160k','-movflags','+faststart','sample_longclip.mp4']
subprocess.run(cmd,check=True)
