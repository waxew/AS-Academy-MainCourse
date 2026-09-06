# درس‌های پایه Backend وب

## درس ۱: Backend دقیقاً چیست؟

### هدف
در پایان درس، هنرجو می‌تواند مسیر یک درخواست را از مرورگر تا سرور و دیتابیس توضیح دهد و مسئولیت Frontend، Backend و Database را تفکیک کند.

### توضیح
Backend بخشی از سامانه است که منطق کسب‌وکار، اعتبارسنجی داده، احراز هویت، کنترل دسترسی، ارتباط با دیتابیس و سرویس‌های بیرونی را اجرا می‌کند. وقتی کاربر روی «ورود» کلیک می‌کند، Frontend اطلاعات را به یک Endpoint می‌فرستد. Backend ورودی را اعتبارسنجی می‌کند، کاربر را از دیتابیس می‌خواند، رمز عبور را با Hash ذخیره‌شده مقایسه می‌کند و در صورت موفقیت Session یا Token معتبر تولید می‌کند.

یک Backend خوب فقط «کدی که جواب JSON می‌دهد» نیست. قرارداد API، امنیت، مدیریت خطا، لاگ، تست، کارایی، قابلیت نگهداری و رفتار درست در شرایط شکست بخشی از طراحی آن هستند.

### مثال جریان درخواست
`Browser -> HTTPS -> Reverse Proxy -> Backend Route -> Validation -> Service -> Repository/ORM -> Database -> Response`

### تمرین
برای یک فروشگاه اینترنتی، مسئولیت‌های Backend در ثبت‌نام، سبد خرید و پرداخت را فهرست کنید.

### معیار پذیرش
پاسخ باید حداقل شامل Validation، Authentication، Database، Authorization و Payment Verification باشد.

## درس ۲: HTTP برای برنامه‌نویس Backend

HTTP یک پروتکل Request/Response است. Method قصد درخواست را بیان می‌کند: GET برای خواندن، POST معمولاً برای ایجاد، PUT/PATCH برای تغییر و DELETE برای حذف. Status Code بخشی از قرارداد API است؛ برای نمونه 200 موفق، 201 ایجاد موفق، 400 ورودی نامعتبر، 401 احراز هویت نشده، 403 فاقد مجوز، 404 پیدا نشد و 500 خطای داخلی است.

Headerها metadata درخواست هستند؛ `Content-Type` نوع Body و `Authorization` معمولاً credential را مشخص می‌کند. در APIهای JSON باید بین خطای Validation، خطای مجوز و خطای داخلی تمایز روشن وجود داشته باشد.

### تمرین
برای CRUD محصول، Method، URI و Status Code مناسب طراحی کنید.

## درس ۳: معماری لایه‌ای ساده

قرار دادن SQL، اعتبارسنجی، منطق پرداخت و ساخت Response در یک Route باعث coupling و دشواری تست می‌شود. ساختار ساده قابل توسعه:

- Route/Controller: دریافت HTTP و تبدیل آن به ورودی برنامه
- Service/Use Case: منطق کسب‌وکار
- Repository: دسترسی به داده
- Model/Entity: مدل دامنه/داده
- Infrastructure: دیتابیس، ایمیل، پیامک، Storage و Providerهای بیرونی

اصل مهم این است که منطق کسب‌وکار تا حد ممکن به HTTP یا یک Vendor خاص وابسته نباشد.

## درس ۴: Validation، Sanitization و Error Handling

هیچ ورودی کاربر قابل اعتماد نیست. نوع، طول، قالب، محدوده و قواعد کسب‌وکار باید در سمت Backend کنترل شوند. Sanitization جای Validation را نمی‌گیرد. خطاهای داخلی نباید Stack Trace یا Secret را به Client نشت دهند. Error Response بهتر است ساختاری پایدار با code، message و field errors داشته باشد.

نمونه قرارداد:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "اطلاعات ورودی معتبر نیست.",
    "fields": {"email": "قالب ایمیل صحیح نیست."}
  }
}
```

## درس ۵: دیتابیس، ORM و Transaction

Backend معمولاً با دیتابیس رابطه‌ای مانند PostgreSQL/MySQL یا دیتابیس‌های دیگر کار می‌کند. ORM سرعت توسعه را بالا می‌برد اما برنامه‌نویس همچنان باید SQL، Index، Join، Transaction و مشکل N+1 را بفهمد. عملیات چندمرحله‌ای که باید «همه یا هیچ» باشند در Transaction قرار می‌گیرند؛ نمونه کلاسیک انتقال اعتبار بین دو حساب است.

## Quiz کوتاه
1. تفاوت 401 و 403 چیست؟
2. چرا Validation فقط در Frontend کافی نیست؟
3. چه زمانی Transaction لازم است؟
4. Service Layer چه مشکلی را حل می‌کند؟
5. چرا نباید Stack Trace را در Production به کاربر نمایش داد؟