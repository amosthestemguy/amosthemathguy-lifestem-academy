# Upload to Bluehost: For Nigerian Schools

The `nigeria/` folder holds the "For Nigerian Schools" page. `send.php` emails each school's request straight to support@countingtocalculus.org.

## Option A: a subdomain, e.g. nigeria.countingtocalculus.org
1. Log in to Bluehost and go to **Websites**, then **Settings** (or **Advanced**, then **cPanel**). Open **Domains**, then **Subdomains**.
2. Create the subdomain `nigeria` on `countingtocalculus.org`. Bluehost makes a folder for it, usually `public_html/nigeria`.
3. Open **cPanel**, then **File Manager**, and go into that folder.
4. Upload `index.html` and `send.php` from this `nigeria/` folder.
5. Turn on free SSL: **Websites**, then **Security**, then SSL, for the new subdomain. It can take up to a few hours.
6. Open https://nigeria.countingtocalculus.org and send a test request. Check that it arrives at support@.

## Option B: a page on the main site, e.g. countingtocalculus.org/nigeria
Upload both files into `public_html/nigeria/` and open https://countingtocalculus.org/nigeria/

## If the test email doesn't arrive
- Check the spam folder.
- In Bluehost **Email**, make sure support@countingtocalculus.org exists or forwards to amostarfa1@gmail.com. The daily check-in reads that Gmail inbox.
- If PHP mail is blocked, the page shows the visitor the email-app and WhatsApp options instead, so no request is lost.
