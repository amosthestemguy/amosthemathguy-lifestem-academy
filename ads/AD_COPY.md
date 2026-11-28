# Counting to Calculus: Facebook & Instagram Video Ads

There are 4 ads. Each is 18.5 seconds long and comes in two sizes, with an original music bed. Every word is on screen, so the ads work with the sound off.

Every ad includes a **live-class scene** that looks like a Zoom gallery view. Amos is at the centre, presenting on a whiteboard where a² + b² = c² is written out by hand, with the history note "known in Babylon, 1800 BC". Student video tiles surround the board and one student raises a hand. The students are clearly drawn as illustrations, and a small caption says so, so no real child's face or name is used. Every ad also closes with Amos's photo and "Classes designed by Amos Tarfa." The Small Group ad opens on the classroom.

| File | Size | Use it for |
|---|---|---|
| `videos/CTC_*_story.mp4` | 1080×1920 (9:16) | Reels, Stories |
| `videos/CTC_*_feed.mp4` | 1080×1350 (4:5) | Facebook and Instagram feeds |

In Ads Manager, upload both sizes to the same ad. Use "Customize media by placement" so each placement shows the right size.

**Landing link for every ad:** `https://tinyurl.com/CountingToCalculus`

---

## Ad 1: "Pick Your Time" (`CTC_times_*`): both offers, built around the schedule
**Primary text**
> Live math and English classes that fit your family's week. 📚
> 🗓 Mon–Thu: 5, 6, 7 or 8 PM ET
> 🗓 Saturday: 12, 1, 2 or 3 PM ET
> Live Class: $300/month per subject (Math or English)
> Small Group (4–6 students): $750/month for Math + Science
> Step 1 is free: a placement assessment that shows exactly where your child is. Month to month, summer included.

**Headline:** Live classes after school & Saturdays
**Description:** Free placement assessment
**Button:** Book Now (or Sign Up)

## Ad 2: "Close the Gaps" (`CTC_gaps_*`): the problem, then the fix. Live Class, $300
**Primary text**
> Schools have to keep moving, so gaps get left behind. The good news: gaps can be fixed.
> 1️⃣ A free placement assessment finds them.
> 2️⃣ Live classes close them. Your child masters each idea before moving on.
> 3️⃣ Your child moves forward, all the way to calculus.
> Live Class: $300/month per subject, Math or English. Mon–Thu 5–8 PM ET, Sat 12–3 PM ET. No contract.

**Headline:** After-school math that builds mastery
**Button:** Book Now

## Ad 3: "Small Group" (`CTC_group_*`): $750
**Primary text**
> 4–6 students. One tutor who knows your child's name and their gaps.
> Small Group includes Math AND Science live every week, a personal learning plan, a monthly 1-on-1 mentor check-in, and help between sessions.
> $750/month. Mon–Thu 5–8 PM ET or Sat 12–3 PM ET. Seats in each group are limited.

**Headline:** 4–6 students. One tutor who knows your child.
**Button:** Sign Up

## Ad 4: "Meet Amos" (`CTC_amos_*`): led by the founder, both offers
**Primary text**
> Top of the class? That's where we start. Being the best in the class is the starting point, not the goal.
> Classes are designed by Amos Tarfa (AmosTheMathGuy), founder of Counting to Calculus and Instructor in the MIT Gateway to AI Initiative.
> Live Class $300/month (Math or English) · Small Group $750/month (Math + Science)
> Mon–Thu 5–8 PM ET · Sat 12–3 PM ET. Start with a free placement assessment.

**Headline:** Top of the class? That's where we start.
**Button:** Learn More

---

## Upgrade: use real classroom footage
A real 5–10 second clip of Amos teaching will outperform any animation. A phone video of you at a whiteboard, or a Zoom recording, both work. To use one:
1. Record yourself at a whiteboard or screen-share. If students appear, use only students whose parents gave written permission for their child to appear in ads. Otherwise use camera-off tiles or blur the faces.
2. Put the clip in `source/` and swap the whiteboard in the `CLASSROOM` block of `source/ad.html` for a `<video>` tile, then re-render.

## A simple plan for launching
1. **Campaign objective:** Leads (or Traffic to the tinyurl form). Budget: start with $10–20 a day.
2. **Run all 4 ads in one ad set for 5–7 days.** Meta will move spending toward the ad that performs best.
3. **Audience:** parents aged 28–55 in the U.S. Start with interests such as homeschooling, tutoring, education and STEM. Choose Eastern and Central time-zone states if live class times matter most.
4. **After a week,** turn off the weakest 2 ads. Make new versions of the winner with a different hook (see the 15 hooks in the Family Recruitment Kit).
5. **Swapping the music:** the music beds are original and free to use. You can also replace them in Ads Manager or Instagram with a track from Meta's Sound Collection, which is licensed for ads. Don't use popular songs; ads that use them get muted or rejected.

## Editing and re-rendering
Edit the words in `source/ad.html` (the `ADS` object), then run:
```
cd ads/source && node render.js times story ../videos/CTC_times_story.mp4
```
The ads are `times`, `gaps`, `group` and `amos`. The sizes are `story` and `feed`. `source/make_music.py` regenerates the music.
