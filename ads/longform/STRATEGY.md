# The 3-version video plan: full video, short and clip

Every recording you make becomes 3 videos. Each one has a different job.

| Version | Length and shape | Where it goes | Its job |
|---|---|---|---|
| **1. Full video** | 20–60 min, 16:9, high quality | YouTube (the right channel for the topic) | The main video. It builds watch time and trust. |
| **2. Short** | 15–60 s, vertical 9:16 | Facebook Reels, Instagram, YouTube Shorts | Reaches people who don't know you yet. |
| **3. Clip** | 3–5 min, 16:9, cut from the full video | YouTube, plus Facebook as a native video | Gives a longer sample of the lesson, then sends people to the full video. |

## What every clip has on screen
- **Top bar:** the channel name, the lesson title and a "CLIP FROM FULL LESSON" badge.
- **Lower third** under Amos's name: "To see the full video, go to our YouTube page". The website and email sit on the right.
- **Captions** burned into the video.
- **An 8-second end card:** "That was just a clip. Watch the full lesson." The empty space at the bottom of the card is left for YouTube end-screen buttons.

## Pointing clip viewers to the full video
1. **First line of the description:** `▶ Full lesson: <link to the full video>`.
2. **YouTube end screen** (set in YouTube Studio, under *Editor* then *End screen*): choose "Video", then "Choose specific video", and pick the full video. It lands in the empty space on the end card.
3. **Pinned comment:** "Full lesson here 👉 <link>".
4. **Clip title:** start with the hook and end with "(clip)". Example: *Newton's Secret Hiding in Squares and Cubes (clip)*.
5. **Link the two together:** in YouTube Studio, set the full video as the clip's *Related video*. Also add the clip to a playlist next to the full video.
6. **Facebook:** use the same description line and post the full-video link as the first comment.

## Order to publish in
1. **Day 1:** the full video.
2. **Days 2–5:** one or two clips, so each points back to a video that is already live.
3. **Days 2–10:** the shorts on Facebook and Instagram, each telling viewers to look for the full video on YouTube.

## Sample
`sample/sample_longclip.mp4`, 5:10 long.
- **Source:** the 48-minute quadratics whiteboard lesson, the part about "the difference of the difference" leading to Newton's derivative.
- **The 4 cuts:** 12:14–13:39, 17:42–18:43, 19:18–21:03 and 21:15–22:06.
- **Left out:** student names and the scheduling talk.

To rebuild it, run `python3 mk.py` from the folder that holds `frame.png`, `end.png` and the source proxy.
