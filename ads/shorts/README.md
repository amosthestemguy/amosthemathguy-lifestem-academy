# "How I Teach" shorts

Five 9:16 shorts (34–62 s), cut from Amos's raw footage in Google Drive ("Unedited" folder). Each has a hook title, captions burned in, a quiet music bed, and a closing card with class times and the link. The prices are at the bottom of the closing card.

| File | Teaching feature | Source |
|---|---|---|
| CTC_short_01_lincoln_euclid.mp4 | The story behind the math | Zoom recording, Nov 1 2026 (00:23:44 UTC) |
| CTC_short_02_perfect_numbers.mp4 | Math is beautiful | Whiteboard, Jul 20 2026 (23:59:13 UTC) |
| CTC_short_03_prerequisites.mp4 | Mastery before speed | Whiteboard, Jul 21 2026 (00:19:12 UTC) |
| CTC_short_04_houston_dallas.mp4 | Real-world math | Whiteboard, Jul 21 2026 (00:38:06 UTC) |
| CTC_short_05_soccer_field.mp4 | Real-world math | Whiteboard, Jul 21 2026 (00:49:54 UTC) |

## Rebuild
1. Download the source clips into a folder.
2. Transcribe them with `source/transcribe.py` (faster-whisper).
3. Run `python3 source/build.py <rawdir> videos`.

To add a new short, add an entry to `SHORTS` in `build.py` with its source clip, start and end seconds, title and feature.
