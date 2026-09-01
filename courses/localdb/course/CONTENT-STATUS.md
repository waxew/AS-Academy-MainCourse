# وضعیت محتوای LocalDB

## نسخه 0.3.0

- معماری Course Package: کامل
- 6 سطح آموزشی و 16 فصل اصلی
- بیش از 30 درس واقعی در سطوح مختلف
- تمرین‌های مقدماتی، متوسط، پیشرفته و تخصصی
- آزمون‌های سطحی و آزمون جامع نهایی
- 7 پروژه عملی از دفترچه تلفن تا حسابداری و Local-first
- واژه‌نامه تخصصی
- اتصال به AS-Academy-Core
- GitHub Actions و Build APK پایدار

## پوشش فعلی

DataStore و Proto DataStore، SQL، SQLiteOpenHelper، Room، DAO/Repository/Flow، CRUD، JOIN/Aggregation، Constraint، Index/Paging/FTS، جست‌وجوی فارسی، Relation، Migration چندنسخه‌ای، Backup/Restore، Security/Keystore/SQLCipher، Testing/Recovery، WAL/VACUUM/Query Plan، Offline-first، Sync Queue، Idempotency و Conflict Resolution پوشش داده شده‌اند.

## کار باقی‌مانده برای Release نهایی

1. QA اجرایی روی Emulator/Device و مسیرهای Back navigation.
2. همگام‌سازی Core pin با آخرین نسخه پایدار پس از QA مشترک همه Courseها.
3. افزایش تعداد سؤال و تمرین در فصل‌های کم‌تراکم.
4. تست نصب نسخه جدید روی نسخه قبلی و حفظ Progress کاربر.
5. ساخت Release APK امضاشده و verify/checksum.

از نظر سرفصل، دوره اکنون نزدیک به نهایی است؛ تمرکز اصلی از این مرحله QA، UX آموزشی و Release Engineering است.
