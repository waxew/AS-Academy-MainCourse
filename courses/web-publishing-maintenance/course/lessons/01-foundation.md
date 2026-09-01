# سطح مبانی — انتشار و نگهداری سایت

## 1. انتشار سایت دقیقاً چیست؟
در محیط توسعه، سایت روی رایانه برنامه‌نویس اجرا می‌شود. انتشار یا Deployment مجموعه کارهایی است که کد، تنظیمات، دارایی‌ها و در صورت نیاز دیتابیس را به محیطی قابل دسترس برای کاربران منتقل می‌کند. Production فقط «آپلود فایل» نیست؛ باید DNS، HTTPS، امنیت، نسخه، Log، Backup و روش بازگشت به نسخه سالم نیز مشخص باشد.

چرخه استاندارد: کد → Build/Test → Artifact → Deploy → Health Check → Monitoring → Feedback/Rollback.

## 2. دامنه، Registrar و DNS
دامنه نام قابل حفظ یک سرویس است. Registrar شرکت ثبت‌کننده دامنه است و DNS نام دامنه را به مقصدهای فنی مانند IP یا سرویس دیگر نگاشت می‌کند.

رکوردهای مهم: A برای IPv4، AAAA برای IPv6، CNAME برای نام مستعار، MX برای ایمیل، TXT برای Verification/SPF و NS برای Name Server. TTL مدت Cache شدن پاسخ DNS است.

## 3. هاست اشتراکی، VPS، Dedicated و Cloud
Shared Hosting ساده‌تر ولی محدودتر است. VPS کنترل مدیریتی بیشتری می‌دهد. Dedicated کل سرور فیزیکی را اختصاص می‌دهد. Cloud معمولاً Provision، Scaling و سرویس Managed را ساده‌تر می‌کند. انتخاب باید بر اساس ترافیک، Backend، دیتابیس، بودجه، SSH، Location، Backup، SLA و مهارت تیم انجام شود.

## 4. IP، Port و Firewall
IP نشانی شبکه و Port نقطه منطقی ورود سرویس است. HTTP معمولاً 80، HTTPS برابر 443 و SSH معمولاً 22 است. امنیت SSH با Authentication قوی، Least Privilege و Firewall ایجاد می‌شود؛ تغییر Port به‌تنهایی امنیت محسوب نمی‌شود.

## 5. HTTP و HTTPS در Production
HTTPS یعنی HTTP روی TLS. TLS محرمانگی، صحت ارتباط و احراز هویت سرور را فراهم می‌کند. Certificate باید معتبر و قابل تمدید باشد. Redirect از HTTP به HTTPS و حذف Mixed Content ضروری است.

## 6. Development، Staging و Production
Development برای توسعه، Staging برای آزمون نزدیک به Production و Production برای کاربران واقعی است. Secret، URL دیتابیس و API Key باید بر اساس محیط مدیریت شوند و Secret واقعی نباید داخل Git Commit شود.

## 7. Versioning و Release
Semantic Versioning قالب MAJOR.MINOR.PATCH دارد. هر Release باید نسخه، تاریخ، تغییرات، Migration لازم و روش Rollback داشته باشد.

## 8. Checklist انتشار
Build/Test، Backup، Environment Variables، Migration، HTTPS/DNS، Health Check، Monitoring، Rollback Plan و بررسی Performance/Security باید قبل از انتشار کنترل شوند.

## تمرین و پروژه
برای یک فروشگاه فرضی Deployment Plan بنویسید: دامنه، DNS، Hosting، محیط‌ها، HTTPS، Backup، Versioning، Monitoring و Rollback را مشخص کنید.
