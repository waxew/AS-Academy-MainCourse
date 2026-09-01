# Android
Internal Storage فضای خصوصی اپ است. برای فایل انتخابی کاربر و اشتراک با برنامه‌های دیگر از Storage Access Framework و URI استفاده می‌شود.

SharedPreferences برای تنظیمات کوچک قدیمی است؛ DataStore asynchronous و مناسب‌تر است. Preferences DataStore کلید/مقدار و Proto DataStore schema تایپ‌دار دارد. داده رابطه‌ای و بزرگ باید در Room باشد.

SQLite دیتابیس embedded است: Schema، CRUD، JOIN، INDEX و TRANSACTION پایه‌های اصلی‌اند. Room روی SQLite شامل Entity، DAO، Database و Repository است و با Coroutines/Flow سازگار است.

Migration باید داده کاربر را حفظ کند و از نسخه‌های واقعی قبلی تست شود. Index برای WHERE/JOIN/ORDER BY پرتکرار مفید است اما Index اضافی write را کند می‌کند.

برای داده حساس، key را hard-code نکنید؛ Android Keystore برای محافظت کلید و SQLCipher برای encryption دیتابیس قابل استفاده است. Backup باید versioned، validate شده و دارای integrity check باشد.

پروژه: مدیریت هزینه با Room+Flow، Relation، Search، Migration v1→v2، Backup JSON و WorkManager Sync با وضعیت PENDING/SYNCED/CONFLICTED.
