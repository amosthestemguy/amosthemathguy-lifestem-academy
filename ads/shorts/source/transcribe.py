import sys, json
from faster_whisper import WhisperModel
import subprocess, numpy as np
def load(p):
    raw=subprocess.run(['ffmpeg','-nostdin','-loglevel','error','-i',p,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768
m = WhisperModel("small.en", device="cpu", compute_type="int8")
for path in sys.argv[1:]:
    segs, info = m.transcribe(load(path), word_timestamps=True, vad_filter=True)
    out = []
    for s in segs:
        out.append({"start": s.start, "end": s.end, "text": s.text.strip(),
                    "words": [{"s": w.start, "e": w.end, "w": w.word} for w in (s.words or [])]})
    json.dump(out, open(path.rsplit('.',1)[0] + '.json', 'w'))
    print("==", path, round(info.duration,1), "s")
    for s in out: print(f"[{s['start']:6.1f}-{s['end']:6.1f}] {s['text']}")
