# Upload to Bluehost: nigeria.countingtocalculus.org

The `nigeria/` folder is the whole "For Nigerian Schools" site:

| File | What it is |
|---|---|
| `index.html` | The hub: order by class, order exam years, request a demo, pay online, prices, contact |
| `order.html` | The order form (`order.html#grades` for every class, `order.html#exams` for Primary 6, JSS 3, SS 3) |
| `demo.html` | Request a demo or a free Maths Health Check |
| `send.php` | Emails each order, pledge and demo request to support@countingtocalculus.org |
| `site.css` | Shared styling |

`nigeria-upload.zip` contains all five files.

## Set up the subdomain (once)
1. Log in to Bluehost. Go to **Websites**, then **Settings** (or **Advanced**, then **cPanel**). Open **Domains**, then **Subdomains**.
2. Create the subdomain `nigeria` on `countingtocalculus.org`. Bluehost makes a folder for it, usually `public_html/nigeria`.
3. Open **cPanel**, then **File Manager**, and go into that folder.
4. Upload `nigeria-upload.zip`, right-click it and choose **Extract**, then delete the zip. All five files should sit directly in the folder (not in a sub-folder).
5. Turn on free SSL for the subdomain: **Websites**, then **Security**, then SSL. It can take a few hours.
6. Open https://nigeria.countingtocalculus.org, then send one test order and one test demo request. Check that both arrive.

## Where the emails go
support@countingtocalculus.org forwards to amosthestemguy@gmail.com. The daily check-in reads amostarfa1@gmail.com, so to have orders, pledges and demo requests logged automatically, add a Gmail filter in amosthestemguy@gmail.com that forwards messages from support@ (or with subjects starting "Book interest pledge" or "School demo request") to amostarfa1@gmail.com.

## If the test email doesn't arrive
- Check the spam folder.
- In Bluehost **Email**, make sure support@countingtocalculus.org exists and forwards as expected.
- If PHP mail is blocked, the page shows the visitor the email-app and WhatsApp options instead, so no request is lost.
