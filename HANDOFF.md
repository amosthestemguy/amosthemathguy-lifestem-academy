# Handoff: Counting to Calculus / LIFE STEM Academy

This document is for whoever continues this work (a person, Manus, or another AI). It explains what exists, where it lives, what is live, and what is still to do. Read it fully before changing anything.

- **Owner:** Amos Tarfa (AmosTheMathGuy)
- **Organisations:** Counting to Calculus (countingtocalculus.org), LIFE STEM Academy, Nigerian School of Mathematics (Counting to Calculus Africa)
- **Repository:** `amosthestemguy/amosthemathguy-lifestem-academy`
- **Working branch:** `claude/sleepy-planck-mwgo7w`. **Nothing on this branch is merged into `main` yet.**
- **Handoff date:** 25 November 2026

---

## 1. Rules you must follow

These are the owner's standing instructions. Do not break them.

1. **No money moves without Amos saying so.** Never turn ads on, change ad budgets, or spend money. Never create Stripe charges or refunds.
2. **No prices in LinkedIn or YouTube captions.** Prices are allowed on Facebook, Instagram and the order pages.
3. **Classics Library posts need approval.** Save them as drafts only; never publish or schedule them without Amos's approval.
4. **Caption style:**
   - Start with a hook.
   - Never use the phrase "keep it simple".
   - On Instagram, write links as plain text.
5. **Contact lines:**
   - General posts: `AmosTheMathGuy.com · Amos@amosthemathguy.com`
   - Classics Library and book posts: `countingtocalculus.org · Support@CountingToCalculus.org`
6. **Video clips start at the start of a problem or a key idea**, never mid-thought.
7. **No secrets in the repository.** No API keys, passwords or `.env` files.
8. **Pair problems with solutions.** When writing for families and teachers, always give concrete steps, not just a description of the problem in math education.

---

## 2. Repository map

| Path | What it is |
|---|---|
| `index.html`, `CNAME` | LIFE STEM Academy website (GitHub Pages, from `main`). `CNAME` says `lifestemacademy.org`, but **that domain is not registered right now**, so the site has no working custom address. |
| `bluehost/` | The site for **nigeria.countingtocalculus.org** (see section 4). |
| `nigeria/index.html` | "For Nigerian Schools" order page. It is the source of a public Claude page (see section 3). |
| `ads/order/` | Public book store page and `STRIPE_LINKS.md` (all 13 live Stripe payment links). |
| `ads/print-tracker/` | Print Tracker: book catalog (`catalog.json`, 39 items) and its page. |
| `ads/dashboard/` | Social media dashboard (posts, channel stats, leads). |
| `ads/tracker/` | `CTC_Social_Media_Posting_Tracker.xlsx`, the posting log. |
| `ads/shorts/` | Vertical short videos: catalog, build scripts (`source/build.py`), finished videos in `library/`. |
| `ads/longform/` | Long-form YouTube strategy (`STRATEGY.md`), the clip builder (`build/mk2.py`) and 12 finished 3–5 minute clips in `clips/`. |
| `ads/images/` | Flyers, the Classics covers collage, the book brochure, and the cut-out covers in `covers/`. |
| `ads/CLASSICS_LIBRARY.md` | Verified facts about the Classics Library (116 editions, 1,319 lessons) and the approval rule. |
| `ads/*.md` | Ad copy, campaign plan, lead playbook, LinkedIn notes. |

---

## 3. What is live right now

### Public pages, hosted as Claude pages on claude.ai

| Page | Link | Who can open it | Source file |
|---|---|---|---|
| Book store (Classics + Nigerian books, cart, Stripe, questions, pledges) | https://claude.ai/artifact/3QMnQt4UB6LCN2tcr9ihW8 | Anyone with the link | `ads/order/index.html` |
| For Nigerian Schools (order by class or exam year) | https://claude.ai/artifact/2VRYAydc7kQVrH24nBPrN7 | Anyone with the link | `nigeria/index.html` |
| Sales demo deck (13 slides, speaker notes) | https://claude.ai/artifact/GnSzKft6H4j5Ce5NHLULkt | Private | Not in the repo |
| Print Tracker | https://claude.ai/artifact/YZHUrUk2bNBCqKfhpC6WTv | Private | `ads/print-tracker/` |

On the claude.ai copies, the question and pledge forms can't send email themselves. The visitor's email app opens instead, with a copy-text fallback. On the Bluehost copy (section 4) these forms send directly.

### Stripe (live mode)
- **Account:** Learning Institute For Excellence LLC, USD.
- **Links:** 13 live payment links, listed in `ads/order/STRIPE_LINKS.md`:
  - 8 Classics volumes at $79.99 each
  - Nigerian textbook $3.65 (≈ ₦5,000)
  - Nigerian workbook $1.80 (≈ ₦2,500)
  - Exam-year textbook $9.25 (≈ ₦12,500)
  - Exam-year workbook $5.50 (≈ ₦7,500)
  - Sample set $7.30 (≈ ₦10,000)
- **Nigerian links:** ship only to Nigeria. Buyers pick their class from a dropdown at checkout and can enter a school name.
- **Classics links:** ship to the US, Canada, the UK and Nigeria.
- **US buyers:** pay in full, no deposit. Shipping is billed separately; the address is collected at checkout. No sales tax.
- **Schools:** pay a 50% deposit, which is arranged by email, not through these links.

### Social media (Posty)
Facebook (Counting To Calculus and LIFE pages), Instagram, LinkedIn and YouTube are connected through Posty.
- **YouTube:** on the trial, Posty allows 1 YouTube post per day.
- **Classics Library launch:** four Posty drafts await Amos's approval (IDs in section 6).

### Daily check-in
A scheduled task called **"Road to 100 – daily check-in"** runs at 9:21 a.m. Mountain Time. It:
- reviews posts and comments
- reads the Gmail inbox **amostarfa1@gmail.com** for Stripe orders, pledges and demo requests, and updates the Print Tracker and dashboard
- follows the rules in section 1

---

## 4. nigeria.countingtocalculus.org (Bluehost), in progress

**Status:** the DNS record is done. Files are **not uploaded yet**.

- **DNS:** an A record `nigeria` → `50.6.21.97` (the Bluehost hosting server) was added and confirmed working on 25 Nov 2026.
  - Main site `countingtocalculus.org` points to `66.235.200.146`. **Do not change it.**
  - Don't touch the domain's MX records; they carry the support@ email.
- **Upload package:** `bluehost/nigeria-upload.zip` (6 files):

| File | Purpose |
|---|---|
| `index.html` | Hub page: order by class, order exam years, request a demo, pay online, gallery of book covers, prices, contact |
| `order.html` | Order form (`#grades` = every class, `#exams` = Primary 6, JSS 3, SS 3) |
| `demo.html` | Request a demo or free Maths Health Check |
| `books.html` | Full book store, the same as the Claude book store page, but its pledges and questions send directly |
| `send.php` | Emails form submissions to support@countingtocalculus.org with PHP `mail()`. It accepts only subjects starting "Book interest pledge", "School demo request" or "Question before ordering", and has a hidden spam-trap field named `website`. |
| `services.html` | Services for Schools: teacher-training tiers (naira + dollars) and a request form |
| `site.css` | Shared styles |
| `covers/` | The 14 class book covers |

- **Remaining steps:** see `bluehost/README.md`. In short:
  1. In cPanel → Domains, create `nigeria.countingtocalculus.org`. Don't share the document root.
  2. In File Manager, upload the zip into that folder and Extract it.
  3. Run AutoSSL.
  4. Send a test order and a test demo request.
- **If email fails:** every form falls back to the visitor's email app and WhatsApp (+234 810 844 1317), so no request is lost.
- **Keep the pages in sync:** `bluehost/nigeria/books.html` is a copy of `ads/order/index.html`, with the "For Nigerian Schools" links changed to `./`. When you change the store, regenerate it:

  ```bash
  sed -e 's#https://claude.ai/artifact/2VRYAydc7kQVrH24nBPrN7#./#g' -e 's#target="_blank" rel="noopener">For Nigerian Schools#>For Nigerian Schools#' ads/order/index.html > bluehost/nigeria/books.html
  ```

- **After go-live:** point links in the Claude pages, the demo deck and the routine to `https://nigeria.countingtocalculus.org`.

---

## 5. Book catalog and printing

### Classics Library ("the secret sauce")
- **8 volumes, $79.99 each.** Pre-order. Ships **2 January 2027**. Buyers get a sample copy by email and can join webinars.
- **Vol 1–4:** Readers for Grades 5–8.
- **Vol 5–8:** Source Books for Grades 9–12, covering the same four eras:
  - Ancient Math History
  - Middle Ages Math History
  - Early Modern Math History
  - Science and Technology History
- **Covers:** the real covers are in `ads/images/covers/cl_v1.jpg` … `cl_v4.jpg`, cut from the collage. Volumes 5–8 reuse the matching era cover. **They need their own Source Book covers.**

### Nigerian School of Mathematics
- **Books:** a textbook and a workbook for every class: Nursery 1, Nursery 2, Primary 1–6, JSS 1–3, SS 1–3.

| Classes | Textbook | Workbook |
|---|---|---|
| Ordinary classes | ₦5,000 | ₦2,500 |
| Exam years (Primary 6, JSS 3, SS 3) | ₦12,500 | ₦7,500 |
| Sample set (one exam year) | ₦10,000 for textbook + workbook | |

- **Printing:** in Abuja, from December. Delivery is before the next term.
- **Covers:** the real front cover for each of the 14 classes is in `ads/images/covers/ng/` and `bluehost/nigeria/covers/` (ng-n1.jpg … ng-ss3.jpg). Workbooks reuse their class cover with an orange "Workbook" corner label until separate workbook covers exist.

### Print rules
- Print runs are **at least 100 copies**, counted across all books combined.
- Schools pay **50% up front**.
- Track every order and pledge in the Print Tracker so nothing is overprinted.

### Order statuses
Pledged → Requested → Deposit paid (50%) → Paid in full → Printed → Delivered (or Cancelled).

### Book IDs
`CL-V1` … `CL-V8`, and `NG-<class>-TB` / `NG-<class>-WB` / `NG-<exam class>-SAMPLE`. The class codes are N1, N2, P1–P6, JSS1–JSS3 and SS1–SS3, so for example `NG-P3-TB`, `NG-JSS3-WB`, `NG-SS3-SAMPLE`.

The order pages and pledge emails use these same IDs. Pledge emails list one book per line as `ID | title | quantity`.

### Orders come from
- email
- website forms
- Facebook messages
- school bulk orders

---

## 6. Pending work, in priority order

1. **Upload the Bluehost site.** The owner is doing this (section 4). Then test it and switch links to the new address.
2. **Gmail forwarding.** support@countingtocalculus.org forwards to **amosthestemguy@gmail.com**, but the daily check-in reads **amostarfa1@gmail.com**.
   - Fix: add a Gmail filter in amosthestemguy@gmail.com that forwards subjects starting "Book interest pledge", "School demo request" or "Question before ordering" to amostarfa1@gmail.com.
   - Until then, pledges are not counted automatically.
3. **Approve the Classics Library launch posts.** These Posty drafts are waiting:

| Channel | Post ID |
|---|---|
| LinkedIn | `cmwwf51c10005ou8j507kjl29` |
| Counting To Calculus Facebook | `cmwwf51dl0006ou8jk3gxsd44` |
| LIFE Facebook | `cmwwf51eo0007ou8jo7x1yxc7` |
| Instagram | `cmwwf51fx0008ou8jn52y8m5d` |

4. **Radesoft International demo request** (contact: Blessing Atolagbe). Book a 30-minute demo within 48 hours, offering 2–3 time slots. Also offer:
   - the free Maths Health Check
   - a sample set
   - the Founding Partner deadline (**31 January 2027**: schools keep today's price for 2027 and 2028)
5. **lifestemacademy.org.** The domain is not registered (the registry returns "no such domain").
   - The owner decides whether to register it, or to use a subdomain of countingtocalculus.org instead.
   - Then update the `CNAME` file and the GitHub Pages settings.
6. **Covers still needed:**
   - separate workbook covers for the Nigerian books (optional)
   - real cover art for Classics Volumes 5–8
7. **Optional: one Stripe link per Nigerian class.** Today one link per book type is shared, and buyers choose the class from a dropdown. Creating per-class links would make 28 new live links; only do it with the owner's approval.
8. **Untranscribed videos.** Four long recordings have no transcript yet: `s007`, `s022`, `s036`, `s045`.
9. **Dashboard.** The "Posted recently" section tries to read live data from Posty. If it doesn't load, revert to the file-based version, which reads `ads/dashboard/data/posts.json`.
10. **Merge to main.** Nothing on `claude/sleepy-planck-mwgo7w` is on `main`. Open a pull request only when the owner asks.

---

## 7. Demo strategy (for the sales team)

- **Individual demos:** within 48 hours of any request.
- **Group webinar for schools:** weekly, at a fixed day and time.
- **Follow-ups:**
  - Day 1: thank you plus the school offer PDF
  - Day 3: sample set or Health Check
  - Day 7: decision call
- **Re-invites:** once a term, plus early January before the 31 January deadline.
- **Weekly target:** 3–5 demos and 1 Health Check booked.
- **Every demo ends with one agreed next step and a date.**

---

## 8. Brand

- **Colours:**

| Name | Hex |
|---|---|
| Navy | `#0B2470` |
| Royal blue | `#1D3FB8` |
| Gold | `#F5B70A` |
| Orange | `#E8762B` |
| Cream | `#F7F4EC` |
| White | `#FFFFFF` |

- **Fonts:** Playfair Display (headings), Inter (body).
- **Taglines:** "No child stuck in mathematics". "Mathematics is not a grade-based subject. It is a mastery-based subject."

### Contacts
- **Email:** support@countingtocalculus.org
- **Nigeria:** Victor Dauda Tarfa, +234 810 844 1317 (Nigeria), +44 7830 123577 (UK)

---

## 9. How to run and check things

- **Pages:** plain HTML, CSS and JavaScript, with no build step. Open them in a browser.
- **`send.php`:** needs a PHP host such as Bluehost. Check it with `php -l bluehost/nigeria/send.php`.
- **Videos:** need ffmpeg and Python. See `ads/shorts/README.md` and `ads/longform/STRATEGY.md`.
- **Before publishing any change:**
  - check at phone width (375px) for sideways scrolling
  - check for JavaScript errors
  - confirm every Stripe link still matches `ads/order/STRIPE_LINKS.md`
