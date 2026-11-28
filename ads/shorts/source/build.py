"""Build captioned 9:16 'How I teach' shorts from raw clips.
python3 build.py <rawdir> <outdir>"""
import json, subprocess, sys, os, re
RAW, OUT = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
HERE = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(HERE, '..', '..', 'music', 'bed_warm.wav')
os.makedirs(OUT, exist_ok=True); TMP = os.path.join(OUT, 'tmp'); os.makedirs(TMP, exist_ok=True)

SHORTS = [
 dict(id='01_lincoln_euclid', feat='The story behind the math',
      title='Abraham Lincoln studied <em>Euclid.</em> Why don’t our kids?',
      segs=[('zoom_1101_002344', 6.0, 64.0)]),
 dict(id='02_perfect_numbers', feat='Math is beautiful',
      title='Why is <em>6</em> a “perfect” number?',
      segs=[('z0720_235913', 1.6, 44.4)]),
 dict(id='03_prerequisites', feat='Mastery before speed',
      title='Every math topic has a <em>prerequisite</em>',
      segs=[('z0721_001912', 42.0, 57.5), ('z0721_001912', 89.4, 116.0)]),
 dict(id='04_houston_dallas', feat='Real-world math',
      title='Add <em>Houston + Dallas</em> and you’re doing real math',
      segs=[('z0721_003806', 3.3, 42.8), ('z0721_003806', 73.6, 80.2)]),
 dict(id='05_soccer_field', feat='Real-world math',
      title='How much paint does a <em>soccer field</em> need?',
      segs=[('z0721_004954', 23.6, 48.6), ('z0721_004954', 82.5, 87.6)]),
]
if len(sys.argv) > 3:
    SHORTS = json.load(open(sys.argv[3]))
VARIANT = sys.argv[4] if len(sys.argv) > 4 else 'social'   # 'social' (9:16, class times + prices) or 'linkedin' (4:5, PD close)
FIXES = {'Leonid': 'Leonhard', 'Benuli': 'Bernoulli', "Benuli's": "Bernoulli's", 'Benulis,': 'Bernoullis,', 'Benulis': 'Bernoullis', 'Joanne': 'Johann', 'Benuli,': 'Bernoulli,', 'air': 'AI', 'fident': 'confident'}
def run(cmd): subprocess.run(cmd, check=True)

def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def captions(sh):
    words, off = [], 0.0
    for seg in sh['segs']:
        src, a, b = seg[:3]
        for seg in json.load(open(os.path.join(RAW, src + '.json'))):
            for w in seg['words']:
                if w['s'] >= a - 0.05 and w['e'] <= b + 0.05:
                    words.append((w['s'] - a + off, w['e'] - a + off, w['w'].strip()))
        off += b - a
    # clean-ups: transcription slips, numbers split at commas, proper nouns
    fixed = []
    for i, w in enumerate(words):
        t = w[2]
        t = FIXES.get(t, t)
        if t == 'Oh' and i + 1 < len(words) and words[i + 1][2].startswith('Euclid'): continue
        if t.startswith('-') and fixed:
            fixed[-1] = (fixed[-1][0], w[1], fixed[-1][2] + t); continue
        if t.startswith(',') and fixed and re.match(r'^[\d,]+$', fixed[-1][2]):
            fixed[-1] = (fixed[-1][0], w[1], fixed[-1][2] + t); continue
        t = t.replace("elements", "Elements") if fixed and fixed[-1][2] == "Euclid's" else t
        fixed.append((w[0], w[1], t))
    words = fixed
    PAIRS = {('great', 'based'): ('grade', 'based'), ('city', 'stud,'): ('C.T.', 'Studd:'), ('Club', 'Maxwell.'): ('Clerk', 'Maxwell.'), ('Club', 'Maxwell'): ('Clerk', 'Maxwell')}
    for k in range(len(words) - 1):
        rep = PAIRS.get((words[k][2], words[k + 1][2]))
        if rep:
            words[k] = (words[k][0], words[k][1], rep[0]); words[k + 1] = (words[k + 1][0], words[k + 1][1], rep[1])
    # chunk into ~3-5 words, break on punctuation / pauses
    chunks, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        gap = words[i + 1][0] - w[1] if i + 1 < len(words) else 9
        if len(cur) >= 5 or (len(cur) >= 2 and re.search(r'[.,?!]$', w[2])) or gap > 0.6:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    lines = []
    for c in chunks:
        txt = ' '.join(x[2] for x in c).replace('{', '').replace('}', '')
        lines.append((c[0][0], c[-1][1] + 0.15, txt))
    fixed = []
    for i, (a, b, txt) in enumerate(lines):
        if i + 1 < len(lines): b = min(b, lines[i + 1][0] - 0.02)
        fixed.append(f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Cap,,0,0,0,,{txt}")
    lines = fixed
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,64,&H00FFFFFF,&H0000B7F5,&H00702408,&H64000000,1,0,0,0,100,100,0,0,1,6,2,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    # position captions centred at y=1275
    lines = [l.replace(',,0,0,0,,', ',,0,0,0,,{\\pos(540,1275)}', 1) for l in lines]
    return head + '\n'.join(lines) + '\n', off

jobs = []
for sh in SHORTS:
    q = dict(feat=sh['feat'], title=sh['title'])
    if VARIANT == 'faith':
        q.update(brand='LIVINGSENSIBLY', pre='LivingSensibly')
    jobs.append(dict(q=q, out=os.path.join(TMP, sh['id'] + '_bg.png')))
jobs.append(dict(q=dict(mode={'linkedin': 'end_li', 'faith': 'end_faith'}.get(VARIANT, 'end')), out=os.path.join(TMP, 'end.png')))
run(['node', os.path.join(HERE, 'cards.js'), json.dumps(jobs)])

for sh in SHORTS:
    sid = sh['id']
    # 1) cut + concat source segments, normalise to 25fps / 48k
    parts = []
    for k, seg in enumerate(sh['segs']):
        src, a, b = seg[:3]; mode = seg[3] if len(seg) > 3 else None
        p = os.path.join(TMP, f'{sid}_p{k}.mp4'); parts.append(p)
        if isinstance(mode, (int, float)):   # vertical phone video: landscape slice centred on the face (fraction of height)
            vf = (f'crop=in_w:in_w:0:min(max(in_h*{mode}-in_w/2\\,0)\\,in_h-in_w),scale=556:556,split[f][g];'
                  '[g]scale=996:996,crop=996:556,boxblur=30:2,eq=brightness=-0.08[bg];[bg][f]overlay=220:0,fps=30,setsar=1')
        elif mode == 'fit':                  # whiteboard: keep the whole board, pad with white
            vf = 'scale=996:556:force_original_aspect_ratio=decrease,pad=996:556:(ow-iw)/2:(oh-ih)/2:white,fps=30,setsar=1'
        else:
            vf = ('crop=in_w:in_h*0.88:0:0,' if src.startswith('zoom') else '' if src.startswith('phone') else 'crop=in_w:in_h*0.935:0:0,') + 'scale=996:556:force_original_aspect_ratio=increase,crop=996:556,fps=30,setsar=1'
        run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(a), '-to', str(b), '-i', os.path.join(RAW, src + '.mp4'),
             '-vf', vf,
             '-af', 'aresample=48000', '-ac', '2', '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', p])
    lst = os.path.join(TMP, sid + '_list.txt')
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    body = os.path.join(TMP, sid + '_body.mp4')
    run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', body])
    ass, dur = captions(sh)
    assf = os.path.join(TMP, sid + '.ass'); open(assf, 'w').write(ass)
    END = 3.5; total = dur + END
    out = os.path.join(OUT, f'CTC_short_{sid}' + {'linkedin': '_LinkedIn_4x5', 'faith': '_LivingSensibly'}.get(VARIANT, '') + '.mp4')
    fc = (
      f"[0:v][2:v]overlay=42:606:shortest=1[v1];[v1]ass={assf}[vb];"
      f"[3:v]trim=duration={END},setpts=PTS-STARTPTS,format=yuv420p,fade=t=in:st=0:d=0.4[ve];"
      f"[vb]format=yuv420p,fade=t=out:st={dur-0.3}:d=0.3[vbf];[vbf][ve]concat=n=2:v=1:a=0" + (",crop=1080:1350:0:190" if VARIANT == 'linkedin' else '') + f"[v];"
      f"[2:a]loudnorm=I=-15:TP=-1.5,apad=pad_dur={END}[voice];"
      f"[4:a]volume=0.10,afade=t=out:st={total-1.5}:d=1.5[mus];"
      f"[voice][mus]amix=inputs=2:duration=first:normalize=0,atrim=0:{total}[a]")
    run(['ffmpeg', '-y', '-loglevel', 'error',
         '-loop', '1', '-framerate', '30', '-t', str(dur), '-i', os.path.join(TMP, sid + '_bg.png'),
         '-f', 'lavfi', '-i', 'anullsrc',
         '-i', body,
         '-loop', '1', '-framerate', '30', '-t', str(END), '-i', os.path.join(TMP, 'end.png'),
         '-stream_loop', '-1', '-i', MUSIC,
         '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
         '-c:v', 'libx264', '-crf', '24', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-t', str(total), out])
    print('built', out, round(total, 1), 's')
