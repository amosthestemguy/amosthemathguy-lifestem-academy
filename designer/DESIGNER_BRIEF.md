# Website Designer Brief: Counting to Calculus, For Nigerian Schools

- **Client:** Amos Tarfa, Counting to Calculus / Learning Institute For Excellence LLC
- **Contact for questions and approvals:** support@countingtocalculus.org
- **Date:** 26 November 2026 (updated: real book covers and Services for Schools page added)

This package contains everything needed to put the Nigerian book site live and improve it. Working pages are already built; your job is to launch them and polish them, without breaking the ordering and payment features described in section 6.

---

## 1. What the site is for

The **Nigerian School of Mathematics** (part of Counting to Calculus) publishes a mathematics textbook and workbook for every class from Nursery 1 to SS 3. The site lets:

- **schools** order books for specific classes or for the exam years, and request a demo or a free Maths Health Check;
- **parents and schools** pay by card, or pledge interest so we know how many copies to print;
- **everyone** see the books, the prices and how ordering works.

It also sells the **Classics Library**, eight books on the history of mathematics, at $79.99 each.

**Success means:** a proprietor on a phone in Nigeria can see the books, understand the price, and send an order or demo request in under two minutes.

---

## 2. Where it lives

| Item | Detail |
|---|---|
| Web address | **https://nigeria.countingtocalculus.org** |
| Hosting | Bluehost (shared hosting with cPanel). The client gives you access. |
| DNS | Already done: an **A** record `nigeria` points to `50.6.21.97`. |
| Do not touch | The main site `countingtocalculus.org`, its `@` and `www` records, and the **MX** records (they carry the support@ email). |
| Technology | Plain HTML, CSS and JavaScript, with one small PHP file for email. No build step, no database, no CMS. |

---

## 3. Files in this package

```
site/            the website, ready to upload
  index.html     home page (hub)
  order.html     order form: #grades (every class) and #exams (exam years)
  demo.html      request a demo or a free Maths Health Check
  books.html     full book store: Classics Library + Nigerian books, cart, card payment, questions, pledges
  services.html  Services for Schools: three teacher-training programmes (naira + dollar prices) and a request form
  send.php       emails each form to support@countingtocalculus.org
  site.css       shared styles for index, order, demo and services
  covers/        the 14 real Nigerian book covers, one per class: ng-n1.jpg, ng-n2.jpg,
                 ng-p1.jpg ... ng-p6.jpg, ng-jss1.jpg ... ng-jss3.jpg, ng-ss1.jpg ... ng-ss3.jpg (600 x 853 px)
assets/
  classics_cover_vol1-4.jpg     real Classics Library covers (Volumes 1-4)
  classics_library_collage.png  all four covers together
STRIPE_LINKS.md  the 13 live card-payment links
DESIGNER_BRIEF   this document
```

---

## 4. Launch steps (about 15 minutes)

1. **cPanel → Domains → Create A New Domain:** `nigeria.countingtocalculus.org`. Untick "Share document root". Note the folder it creates.
2. **File Manager:** upload everything in `site/` into that folder, including the `covers` folder, so `index.html` and `covers/` sit directly in it, not in a sub-folder.
3. **SSL/TLS Status:** tick the subdomain and click **Run AutoSSL**.
4. **Test:** work through the checklist in section 9.

---

## 5. Brand guide

### Colours

| Name | Hex | Use |
|---|---|---|
| Navy | `#0B2470` | Headers, main buttons, text |
| Royal blue | `#1D3FB8` | Textbook covers, accents |
| Gold | `#F5B70A` | Highlights, footer, exam-year books |
| Orange | `#E8762B` | Workbook covers, accents |
| Cream | `#F7F4EC` | Page background |
| White | `#FFFFFF` | Cards, text on navy |

### Fonts
- **Playfair Display** (bold, 700/900) for headings.
- **Inter** (400–800) for body text and buttons.
- Both come from Google Fonts.

### Taglines
- "No child stuck in mathematics"
- "Mathematics is not a grade-based subject. It is a mastery-based subject."
- "Three books, one story from counting to calculus."

### Tone
Warm, confident and plain. Short sentences. Speak to proprietors, head teachers and parents. Always pair a problem with a clear next step.

### Contact block (use exactly)
- support@countingtocalculus.org
- Call or WhatsApp Victor Dauda Tarfa: +234 810 844 1317 (Nigeria) · +44 7830 123577 (UK)
- CountingToCalculus.org

---

## 6. Things that must keep working: do not change without approval

The client's ordering, printing and reporting depend on these. Change the look as much as you like, but keep these exactly as they are.

1. **Payment links.** Every "Buy now" and "Pay" button uses a live Stripe link from `STRIPE_LINKS.md`. Do not edit, shorten or replace these URLs.
2. **Prices.** Prices change only with written approval from the client.
3. **The email subjects.** `send.php` only accepts messages whose subject starts with one of these, and the client's order tracking reads them:
   - `Book interest pledge:`
   - `School demo request:`
   - `Question before ordering:`
4. **The pledge lines.** Pledge emails list one book per line as `ID | title | quantity`, and the book IDs (for example `NG-P3-TB`, `NG-JSS3-WB`, `CL-V1`) must stay the same. They match the client's print-tracking catalog.
5. **`send.php`.** Keep the recipient (`support@countingtocalculus.org`) and the hidden spam-trap field named `website`.
6. **The fall-back.** If the server can't send an email, each form shows the visitor an "Open my email app" and a "Send on WhatsApp" option instead, so no order is lost. Keep it.
7. **No tracking, pop-ups or third-party scripts** (analytics, chat widgets, ad pixels) without the client's approval.
8. **No passwords or API keys** in any file.

---

## 7. Prices (as shown on the site)

| Classes | Textbook | Workbook |
|---|---|---|
| Nursery 1, Nursery 2, Primary 1–5, JSS 1, JSS 2, SS 1, SS 2 | ₦5,000 ($3.65) | ₦2,500 ($1.80) |
| Exam years: Primary 6 (Common Entrance), JSS 3 (BECE), SS 3 (WAEC, NECO, JAMB) | ₦12,500 ($9.25) | ₦7,500 ($5.50) |
| Sample set, any exam year (textbook + workbook) | ₦10,000 ($7.30) | |
| Classics Library, Volumes 1–8 | $79.99 each | |

### How ordering works
1. The school sends its classes and number of pupils.
2. We confirm the order, price and delivery date in writing.
3. The school pays a 50% deposit; the balance is due on delivery.
4. Printing in Abuja from December.
5. Delivery before the next term.

### Offers
- **Founding Partner:** schools that join by 31 January 2027 keep today's price for 2027 and 2028.
- **Teacher training:** termly cluster training and monthly online coaching.
- **Free Maths Health Check:** one class, with a one-page results report.

### Services for Schools (teacher training, `services.html`)
Prices in naira with the US dollar equivalent at ₦1,350 = $1. Do not change them without approval.

| Programme | Price |
|---|---|
| Tier 1: CTC Launch Workshop | ₦75,000 per school (≈ $56). ₦25,000 (≈ $19) credited back with a qualifying book order within 14 days |
| Tier 2: Implementation Programme (flagship) | ₦225,000 per school (≈ $167) |
| Tier 3: Maths Excellence Partnership | ₦450,000 per term (≈ $333). Early-adopter pilot ₦375,000 (≈ $278) for the first 10 schools |

The training request form sends a subject starting `School demo request:` with "(Teacher training: Tier …)", so it uses the same email route as demo requests.

---

## 8. What we would like from you, in priority order

1. **Launch** the site (section 4) and pass the test checklist (section 9).
2. **Nigerian book covers: done.** The real front cover for each of the 14 classes is now in `site/covers/` and shows on every page (book store, order form, home page gallery). Each class has one cover, so the workbook card reuses the textbook cover with an orange "Workbook" corner label (the `.ngc-tag` element). If separate workbook covers are made later, save them as `covers/ng-<class>-wb.jpg` at the same size (600 × 853 px, under 100 KB) and point the workbook `<img>` tags to them; keep the alt text pattern, e.g. `alt="Primary 3 Mathematics, Nigerian School of Mathematics, workbook cover"`.
3. **Covers for Classics Library Volumes 5–8** (the Grade 9–12 Source Books). They currently reuse the Volume 1–4 covers.
4. **Visual polish:**
   - a hero image or photo of children learning for the home page
   - consistent spacing
   - a favicon and logo
5. **Search and sharing:** page titles and descriptions, and an Open Graph image (1200 × 630) so links look good on WhatsApp and Facebook.
6. **Speed for Nigerian mobile data:**
   - compress images
   - avoid large libraries
   - keep each page under about 1 MB

### Must also be true
- Works well on a phone at 360–390 px wide, with no sideways scrolling.
- Readable in bright sunlight: strong contrast, text at least 16 px.
- Every form field has a label. Buttons are at least 44 px tall.

---

## 9. Test checklist before you hand over

1. https://nigeria.countingtocalculus.org opens with the padlock (https).
2. All the buttons on the home page open the right pages, and every book cover image loads.
3. **Order for specific grade levels.** Send a test order with school name "TEST – please ignore". The page says it was sent, and an email arrives at support@ with a subject starting "Book interest pledge:".
4. **Request a demo.** Send a test request. The email arrives with "School demo request:". Do the same from **Services for Schools** (`services.html`): pick a tier and send.
5. **books.html.** Then:
   - Add a book to the cart.
   - Open **Pay**. It must reach the Stripe checkout page. Don't complete payment.
   - Send a test pledge and a test question. Both emails arrive.
6. Check every page on a phone, on a laptop, and in Chrome and Safari.
7. Tell the client when the tests pass, so they can delete the test emails and announce the link.

---

## 10. Who approves what

| Decision | Who |
|---|---|
| Prices, offers, payment links | The client only |
| Wording of offers and policies | The client |
| Layout, colours within the brand, images, fonts | You, then the client reviews |
| Anything touching DNS, email or the main countingtocalculus.org site | Ask the client first |
