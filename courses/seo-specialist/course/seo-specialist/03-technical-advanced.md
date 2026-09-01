# سطح ۳ و ۴ — Technical و Advanced SEO

## robots.txt
robots.txt عمدتاً Crawl را کنترل می‌کند و جایگزین noindex نیست. قبل از Block کردن مسیر باید بررسی شود آیا Google برای Rendering صفحه به Resourceهای آن مسیر نیاز دارد یا خیر.

## XML Sitemap
Sitemap باید URLهای Canonical و قابل Index را فهرست کند. تقسیم Sitemapهای بزرگ بر اساس نوع محتوا تحلیل خطا را آسان‌تر می‌کند.

## Canonical
Canonical برای اعلام نسخه ترجیحی میان صفحات مشابه/تکراری است. canonical اشتباه می‌تواند سیگنال‌ها را به URL نامناسب منتقل کند. Canonical باید همراه Redirect، Sitemap و Internal Links از نظر Consistency بررسی شود.

## Redirect و Status Codes
301/308 برای انتقال پایدار، 302/307 برای انتقال موقت و 404/410 برای منابع حذف‌شده کاربرد دارند. Redirect Chain و Loop باید حذف شوند. Soft 404 نیز باید بررسی شود.

## Crawl Budget و معماری
برای سایت‌های بزرگ، URLهای پارامتری، Faceted Navigation، تقویم بی‌نهایت، Session ID و صفحات کم‌ارزش می‌توانند فضای Crawl را هدر دهند. معماری کم‌عمق و Internal Linking منطقی کشف صفحات مهم را تسهیل می‌کند.

## Structured Data
JSON-LD روش رایج پیاده‌سازی است. Markup باید محتوای قابل مشاهده صفحه را درست توصیف کند و مطابق Eligibility هر Rich Result باشد. تست صحت Syntax به تنهایی تضمین نمایش Rich Result نیست.

## Core Web Vitals
- LCP: سرعت نمایش محتوای اصلی.
- INP: پاسخ‌گویی به تعاملات کاربر.
- CLS: ثبات بصری Layout.
داده Field و Lab باید از هم تفکیک شوند. PageSpeed Insights، Chrome UX Report و DevTools برای تحلیل مکمل‌اند.

## JavaScript SEO
CSR، SSR و SSG را مقایسه کنید. بررسی کنید HTML اولیه چه محتوایی دارد، لینک‌ها با href واقعی قابل کشف هستند یا خیر، Metadata و Canonical سمت سرور صحیح‌اند، Lazy Loading محتوای حیاتی را پنهان نمی‌کند و Errorهای JS مانع Render نمی‌شوند.

## Semantic و Entity SEO
به جای تولید صفحات متعدد برای Variations نزدیک Keyword، Topic را جامع مدل کنید. Entityها، روابط مفهومی، Terminology دقیق، ساختار اطلاعات و Internal Linking باید به فهم موضوع کمک کنند. «Semantic SEO» مجوز تولید متن حجیم و تکراری نیست.

## E-E-A-T
Experience، Expertise، Authoritativeness و Trust چارچوبی برای ارزیابی کیفیت است؛ به‌خصوص Trust اهمیت محوری دارد. برای موضوعات حساس، شفافیت نویسنده، منابع، سیاست‌های سایت و دقت محتوا اهمیت بیشتری پیدا می‌کند.

## Link Building
کیفیت و ارتباط لینک مهم‌تر از شمار خام لینک‌هاست. Digital PR، Assets قابل استناد، Research، Partnerships و Outreach واقعی نسبت به خرید انبوه لینک پایدارترند. Anchor Text غیرطبیعی و Link Scheme ریسک Spam Policy دارند.

## تمرین Audit
یک سایت را با Crawler بررسی و حداقل این موارد را گزارش کنید: status codes، redirect chains، canonicals، noindex، robots directives، orphan/deep pages، duplicate titles، thin pages، structured data، CWV و internal link depth. هر Issue باید Severity، Evidence، Impact و Recommended Fix داشته باشد.
