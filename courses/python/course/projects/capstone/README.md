# Capstone نهایی Python — سیستم مدیریت فروش و مشتری

این پروژه آزمون نهایی دوره است. هنرجو باید بدون کپی‌کردن یک راه‌حل آماده، سیستم را مرحله‌به‌مرحله طراحی و پیاده‌سازی کند.

## هدف
ساخت یک Backend واقعی برای مدیریت Customer، Product، Inventory، Invoice و Payment با Python.

## مرحله 1 — تحلیل دامنه
Entityها و قوانین را قبل از کدنویسی مشخص کنید.

حداقل مدل‌ها:
- Customer
- Product
- InventoryItem
- Invoice
- InvoiceItem
- Payment
- User

قوانین نمونه:
- قیمت و تعداد منفی ممنوع.
- Invoice بدون item قابل نهایی‌شدن نیست.
- فروش بیشتر از موجودی ممنوع.
- عملیات مالی مرتبط باید transaction داشته باشند.

## مرحله 2 — Database
PostgreSQL و migration استفاده شود.

موارد اجباری:
- Primary/Foreign Key
- Constraint
- Indexهای ضروری
- Relationship
- Transaction
- Migration

## مرحله 3 — معماری
```text
API Route
   ↓
Validation Schema
   ↓
Service / Use Case
   ↓
Repository
   ↓
Database
```

منطق business نباید داخل route یا ORM model پراکنده شود.

## مرحله 4 — REST API
حداقل endpointها:
- Auth login
- Customer CRUD
- Product CRUD
- Inventory adjustment
- Invoice create/read/list
- Payment registration
- Sales report

برای status code و error response قرارداد یکنواخت تعریف کنید.

## مرحله 5 — Authentication و Authorization
- password hashing مناسب
- access token
- role/permission
- secret از environment
- عدم ثبت token/password در log

## مرحله 6 — Testing
حداقل:
- Unit test برای serviceها
- Integration test برای repository/API
- Parametrized validation tests
- Fake/Mock برای dependencyهای خارجی
- تست transaction failure

## مرحله 7 — Logging و Observability
رخدادهای مهم ثبت شوند، اما داده حساس log نشود.

Health endpoint و اطلاعات لازم برای تشخیص خطا در production اضافه شود.

## مرحله 8 — Docker
- Dockerfile
- compose برای API و PostgreSQL
- environment configuration
- volume دیتابیس
- health check

## مرحله 9 — CI
Pipeline پیشنهادی:
```text
Commit -> Lint -> Test -> Build -> Security/Dependency Check -> Deploy Candidate
```

## مرحله 10 — مستندات
README باید شامل نصب، config، migration، اجرای test، اجرای Docker، API overview و معماری باشد.

## معیار ارزیابی
- Domain design: 15%
- Database: 15%
- API design: 15%
- Security: 10%
- Tests: 15%
- Architecture/code quality: 15%
- Deployment/CI: 10%
- Documentation: 5%

حداقل امتیاز قبولی: 70 از 100.

## مسیر توسعه تخصصی اختیاری
پس از تکمیل نسخه اصلی یکی از مسیرها را اضافه کنید:
1. Dashboard تحلیلی با Pandas
2. Desktop Admin Client
3. Telegram notification bot
4. ML sales prediction
5. RAG assistant روی مستندات و داده‌های مجاز سیستم

هدف Capstone این است که هنرجو ثابت کند می‌تواند مفاهیم دوره را در یک سیستم منسجم و قابل استقرار ترکیب کند.