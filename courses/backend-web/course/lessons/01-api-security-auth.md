# Authentication، Authorization و امنیت API

## Authentication در برابر Authorization
Authentication پاسخ می‌دهد «کاربر چه کسی است؟» و Authorization پاسخ می‌دهد «این هویت اجازه انجام چه کاری دارد؟». ورود موفق نباید به معنی دسترسی کامل باشد.

## ذخیره رمز عبور
رمز عبور نباید plaintext یا با encryption برگشت‌پذیر ذخیره شود. از password hashing مناسب مانند Argon2 یا bcrypt با تنظیمات هزینه مناسب استفاده می‌شود. Salt باید طبق پیاده‌سازی استاندارد الگوریتم مدیریت شود.

## Session
در مدل Session، سرور شناسه Session را نگه می‌دارد و Client معمولاً cookie شناسه را ارسال می‌کند. Cookie احراز هویت باید با گزینه‌های امنیتی مناسب مانند HttpOnly، Secure و SameSite تنظیم شود. برای درخواست‌های مبتنی بر Cookie، CSRF باید در مدل تهدید لحاظ شود.

## JWT
JWT یک قالب Token است، نه یک سامانه کامل Authentication. Access Token بهتر است کوتاه‌عمر باشد. Refresh Token نیازمند طراحی rotation/revocation و نگهداری امن است. داده محرمانه نباید صرفاً به دلیل Base64 بودن payload داخل JWT قرار گیرد.

## RBAC
در Role-Based Access Control مجوزها به Roleها متصل می‌شوند. برای سامانه فروشگاهی می‌توان `customer`, `staff`, `manager`, `admin` تعریف کرد، اما Endpoint باید Permission واقعی عملیات را بررسی کند و صرفاً به مخفی بودن دکمه در UI اعتماد نکند.

## Rate Limiting
Endpointهای Login، OTP، Password Reset و API عمومی اهداف رایج abuse هستند. Rate Limiting باید با کلید مناسب مثل IP، user/tenant یا ترکیبی از آن‌ها طراحی شود و در سامانه چندسروری Store مشترک مانند Redis می‌تواند لازم باشد.

## CORS
CORS مکانیزم مرورگر برای کنترل دسترسی cross-origin است و جای Authentication یا Authorization را نمی‌گیرد. `Access-Control-Allow-Origin: *` نباید بدون درک اثر آن، مخصوصاً همراه credential، استفاده شود.

## Upload امن
نام فایل کاربر را مسیر فایل سیستم فرض نکنید. Type واقعی، اندازه، extension، محل ذخیره و سطح دسترسی باید کنترل شود. فایل‌های حساس بهتر است public مستقیم نباشند و با Signed URL یا Endpoint مجاز تحویل شوند.

## تمرین پروژه‌ای
برای API سامانه نوبت‌دهی، Endpointهای ثبت‌نام، ورود، Refresh Token، مشاهده نوبت، ایجاد نوبت و مدیریت کارکنان را طراحی کنید. برای هر Endpoint مشخص کنید چه Role/Permission لازم است، چه Rate Limitی منطقی است و چه داده‌ای باید Audit شود.

## Quiz
1. JWT چه تفاوتی با Session دارد؟
2. چرا Access Token طولانی‌عمر ریسک دارد؟
3. CORS چرا Authorization نیست؟
4. چه Endpointهایی معمولاً Rate Limit سخت‌گیرانه‌تری می‌خواهند؟
5. چرا کنترل دسترسی در Frontend کافی نیست؟