# سطح پیشرفته — Docker، CI/CD، امنیت، Performance و SEO

## Docker
Docker Image قالب immutable برای اجرای برنامه و Container نمونه اجرای آن است. Dockerfile باید تا حد ممکن کوچک، قابل بازتولید و بدون Secret باشد. Multi-stage build برای جدا کردن ابزار Build از Runtime مفید است.

Volume برای داده پایدار و Network برای ارتباط سرویس‌هاست. Database production را بدون سیاست Backup و Persistence در Container رها نکنید.

## Docker Compose
Compose چند سرویس مانند web، api، database و cache را تعریف می‌کند. Healthcheck، restart policy، volume و network را مشخص کنید. فایل Production باید از Secret واقعی محافظت کند و Imageها را به نسخه مشخص Pin کند.

## CI/CD
Continuous Integration یعنی ادغام مکرر همراه Build/Test خودکار. Continuous Delivery/Deployment مسیر انتشار را خودکار می‌کند. Pipeline نمونه: Checkout → Install → Lint → Test → Build → Security Scan → Artifact → Deploy Staging → Smoke Test → Approval → Production → Health Check.

Secretها را در GitHub Actions Secrets/Environment یا Secret Manager نگه دارید. Permission توکن Workflow را حداقلی کنید. Environment Protection می‌تواند Deploy Production را نیازمند Approval کند.

## Rollback و Artifact
همان Artifact تست‌شده را به Production ببرید؛ روی سرور دوباره Build تصادفی انجام ندهید. نسخه قبلی سالم را نگه دارید تا Rollback سریع باشد.

## Logging و Monitoring
Log باید زمان، severity، service، request/correlation id و context مفید داشته باشد و Password/Token/اطلاعات حساس را ثبت نکند. Monitoring شامل Uptime، latency، error rate، CPU، RAM، disk، queue و شاخص‌های کسب‌وکار مهم است.

Alert باید actionable باشد. هشدار زیاد بدون اقدام باعث Alert Fatigue می‌شود.

## OWASP Top 10 2025
دوره ریسک‌های اصلی نسخه 2025 را پوشش می‌دهد: Broken Access Control، Security Misconfiguration، Software Supply Chain Failures، Cryptographic Failures، Injection، Insecure Design، Authentication Failures، Software or Data Integrity Failures، Security Logging and Alerting Failures و Mishandling of Exceptional Conditions.

برای هر ریسک سه سؤال: حمله چگونه رخ می‌دهد؟ کنترل پیشگیرانه چیست؟ چگونه تشخیص/مانیتور می‌شود؟

## Hardening
Least Privilege، Patch منظم، حذف سرویس غیرضروری، Secret Rotation، Headerهای امنیتی، محدودسازی Upload، Rate Limiting، Validation، Dependency Update و Backup امن را ترکیب کنید. WAF یک لایه کمکی است و ضعف کد را درمان نمی‌کند.

## Performance و Core Web Vitals
سه شاخص اصلی تجربه کاربری: LCP برای سرعت نمایش محتوای اصلی، INP برای responsiveness تعامل و CLS برای پایداری بصری. اندازه‌گیری Field Data و Lab Data مکمل یکدیگرند.

بهینه‌سازی‌ها: کاهش TTFB، Cache مناسب، CDN، Compression، حذف JavaScript غیرضروری، lazy loading هدفمند، ابعاد صریح تصویر، فرمت تصویر مناسب، preload محدود منابع حیاتی، بهینه‌سازی Font و جلوگیری از Layout Shift.

## Cache
Browser Cache، Reverse Proxy Cache، CDN Cache و Application Cache سطوح متفاوت‌اند. Cache-Control و validation را بفهمید. داده شخصی یا پاسخ authenticated نباید بدون سیاست دقیق وارد Cache عمومی شود.

## HTTP/2 و HTTP/3
HTTP/2 multiplexing را روی یک connection بهبود می‌دهد. HTTP/3 روی QUIC است. فعال‌سازی پروتکل جدید بدون اندازه‌گیری به‌تنهایی Performance را تضمین نمی‌کند.

## SEO فنی
Crawlability و Indexability را بررسی کنید. robots.txt دستور Crawl است و ابزار قطعی حذف از Index نیست. XML Sitemap URLهای canonical مهم را معرفی می‌کند. Canonical برای ترجیح نسخه اصلی URL، Redirect برای انتقال واقعی و Status Code صحیح برای معنای پاسخ استفاده می‌شود.

Structured Data باید با محتوای واقعی صفحه منطبق باشد. لینک داخلی، معماری اطلاعات، Mobile usability، سرعت و HTML معنایی روی قابلیت کشف و تجربه اثر دارند.

## SEO محتوایی
هدف جستجو، کیفیت و اصالت محتوا، ساختار Heading، عنوان و Description مفید، لینک داخلی و به‌روزرسانی محتوای قدیمی مهم‌اند. Keyword stuffing راهبرد مناسب نیست.

## GA4 و Analytics
Measurement Plan را قبل از Tagging تعریف کنید: چه Eventهایی و چرا؟ Page view، signup، purchase و conversion نمونه‌اند. از جمع‌آوری داده اضافی و PII بدون مبنای مناسب خودداری کنید. Debug و صحت Eventها را قبل از تصمیم‌گیری تجاری بررسی کنید.

## Search Console
Coverage/Indexing، Sitemap، Performance Search و مشکلات فنی را برای پایش حضور در جستجو استفاده کنید. داده Search Console و Analytics هدف یکسانی ندارند و باید مکمل تحلیل باشند.

## Cookie و Privacy
Cookieهای ضروری را از Analytics/Advertising تفکیک کنید. Consent باید با قوانین حوزه فعالیت و ابزارهای واقعی سایت سازگار باشد. Data Minimization، Retention و امکان تغییر انتخاب کاربر را در طراحی لحاظ کنید.

## پروژه پیشرفته
یک Pipeline کامل برای Frontend+Backend طراحی کنید: Docker image، تست، Security check، Registry، Staging، Approval، Production، Health Check، Rollback، Monitoring و Release Notes. سپس Lighthouse/Core Web Vitals و Technical SEO را Audit کنید.
