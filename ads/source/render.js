// node render.js <ad> <fmt> <out.mp4|--stills dir> [fps]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const [ad, fmt, out, fpsArg] = process.argv.slice(2);
const FPS = +(fpsArg || 30);
const SIZE = fmt === 'story' ? { width: 540, height: 960 } : { width: 540, height: 675 };
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: SIZE, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(__dirname, 'ad.html') + `?ad=${ad}&fmt=${fmt}`);
  await page.evaluate(() => window.READY);
  const total = await page.evaluate(() => window.TOTAL);
  if (out === '--stills') {
    const dir = process.argv[6];
    for (const t of [1.6, 6.0, 9.6, 13.5].map(x => x * total / 15)) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: `${dir}/${ad}_${fmt}_${t.toFixed(1)}.png`, scale: 'css' });
    }
  } else {
    const music = path.resolve(__dirname, '..', 'music', `bed_${await page.evaluate(() => window.MUSIC)}.wav`);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-i', music, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
      '-profile:v', 'high', '-movflags', '+faststart', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.round(total * FPS);
    for (let i = 0; i < n; i++) {
      await page.evaluate(t => window.render(t), i / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    console.log('done', out);
  }
  await browser.close();
})();
