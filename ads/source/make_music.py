"""Original, royalty-free music beds for the Counting to Calculus ads.
Usage: python3 make_music.py OUT.wav SECONDS BPM VARIANT
VARIANT 0 = bright/uplifting (C major), 1 = warm/confident (A minor -> C)."""
import sys, numpy as np, wave

SR = 44100
out, dur, bpm, var = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
N = int(SR * dur)
t = np.arange(N) / SR
beat = 60.0 / bpm
bar = 4 * beat
mix = np.zeros((N, 2))

def midi(n): return 440.0 * 2 ** ((n - 69) / 12)

# chord progressions (midi notes, root first)
if var == 0:   # C  G  Am  F
    prog = [[48, 60, 64, 67], [43, 59, 62, 67], [45, 60, 64, 69], [41, 60, 65, 69]]
else:          # Am F  C  G
    prog = [[45, 60, 64, 69], [41, 60, 65, 69], [48, 60, 64, 67], [43, 59, 62, 67]]

def add(sig, start, pan=0.0, gain=1.0):
    i = int(start * SR)
    if i >= N: return
    sig = sig[: N - i] * gain
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    mix[i:i + len(sig), 0] += sig * l
    mix[i:i + len(sig), 1] += sig * r

def env(n, a, d, s, r, length):
    e = np.ones(n) * s
    A, D, R = int(a * SR), int(d * SR), int(r * SR)
    e[:A] = np.linspace(0, 1, A)
    e[A:A + D] = np.linspace(1, s, D)
    rel = int(length * SR)
    if rel < n:
        e[rel:rel + R] = np.linspace(s, 0, min(R, n - rel))[: len(e[rel:rel + R])]
        e[rel + R:] = 0
    return e

def pad(freq, length):
    n = int((length + 0.8) * SR); tt = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * freq * k * (1 + dt) * tt) / k ** 1.6
            for k in (1, 2, 3, 4) for dt in (-0.003, 0.003))
    return s * env(n, 0.5, 0.4, 0.7, 0.8, length) * 0.5

def pluck(freq, length=0.6):
    n = int(length * SR); tt = np.arange(n) / SR
    s = (np.sin(2 * np.pi * freq * tt) + 0.35 * np.sin(4 * np.pi * freq * tt)
         + 0.12 * np.sin(6 * np.pi * freq * tt))
    return s * np.exp(-tt * 7) * np.minimum(1, tt * 400)

def bass(freq, length):
    n = int(length * SR); tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * tt) + 0.25 * np.sin(4 * np.pi * freq * tt)
    return s * np.minimum(1, tt * 80) * np.exp(-tt * 1.2) * np.minimum(1, (length - tt) * 30)

def kick():
    n = int(0.35 * SR); tt = np.arange(n) / SR
    f = 50 + 90 * np.exp(-tt * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)

rng = np.random.default_rng(7)
def hat(length=0.06):
    n = int(length * SR); tt = np.arange(n) / SR
    w = rng.standard_normal(n); w = np.diff(w, prepend=0)  # crude high-pass
    return w * np.exp(-tt * 70) * 0.5

def clap():
    n = int(0.2 * SR); tt = np.arange(n) / SR
    return rng.standard_normal(n) * np.exp(-tt * 25) * 0.4

nbars = int(np.ceil(dur / bar)) + 1
arp_pattern = [1, 2, 3, 2, 1, 2, 3, 2] if var == 0 else [1, 3, 2, 3, 1, 3, 2, 3]
for b in range(nbars):
    ch = prog[b % 4]; t0 = b * bar
    for nt in ch[1:]:
        add(pad(midi(nt), bar), t0, pan=rng.uniform(-0.5, 0.5), gain=0.11)
    # bass: root on 1 and the "and" of 2
    add(bass(midi(ch[0] - 12 + 12), beat * 1.5), t0, gain=0.42)
    add(bass(midi(ch[0] - 12 + 12), beat * 2.4), t0 + beat * 1.5, gain=0.34)
    # 8th-note plucked arpeggio, an octave up (enters after first bar)
    if b >= 1 or var == 1:
        for k in range(8):
            nt = ch[arp_pattern[k]] + 12
            add(pluck(midi(nt)), t0 + k * beat / 2, pan=(-0.35 if k % 2 else 0.35), gain=0.16)
    # drums (enter after first half bar)
    for k in range(4):
        tb = t0 + k * beat
        if tb < bar * 0.5: continue
        if k in (0, 2): add(kick(), tb, gain=0.55)
        if k in (1, 3): add(clap(), tb, gain=0.22)
        add(hat(), tb + beat / 2, pan=0.2, gain=0.35)
        add(hat(0.03), tb, pan=-0.2, gain=0.15)

# soft one-pole low-pass on the master for warmth
alpha = 0.55
for c in range(2):
    y = mix[:, c]; z = np.empty_like(y); acc = 0.0
    # vectorised approximation via lfilter-like loop in chunks
    for i in range(len(y)):
        acc += alpha * (y[i] - acc); z[i] = acc
    mix[:, c] = z

# fades
fi, fo = int(0.25 * SR), int(1.4 * SR)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]
mix[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 1.5
mix = np.tanh(mix / (np.abs(mix).max() + 1e-9) * 1.4) * 0.85
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes())
print('wrote', out)
