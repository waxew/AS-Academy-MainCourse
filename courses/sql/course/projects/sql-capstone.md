# پروژه نهایی جامع SQL

یک سامانه فروش، انبار و حسابداری کوچک طراحی کنید.

## دامنه
Customer، Product، Category، Inventory، Order، OrderItem، Payment، Account و LedgerEntry.

## الزامات
- ERD و توضیح cardinality رابطه‌ها
- Schema و Naming Convention
- Primary/Foreign/Composite Key و Constraintهای لازم
- Seed Data قابل آزمایش
- CRUD کامل
- گزارش فروش، مشتریان برتر، موجودی کم و گردش حساب
- حداقل یک CTE و یک Window Function واقعی
- View برای گزارش خواندنی
- Function/Procedure متناسب با DBMS انتخابی
- Trigger فقط در سناریویی که دلیل معماری روشن دارد
- Transaction برای ثبت سفارش/پرداخت
- سناریوی concurrent update و توضیح راه‌حل
- Indexگذاری بر اساس workload
- ثبت و تحلیل Execution Plan قبل و بعد از Optimization
- جلوگیری از SQL Injection با Parameterized Query
- Role و Least Privilege
- Backup/Restore plan
- مقایسه نحوه اجرای پروژه روی PostgreSQL، MySQL یا SQL Server

## خروجی آموزشی
دانشجو باید علاوه بر فایل SQL، توضیح دهد چرا هر Constraint، Index و Transaction انتخاب شده است. امتیاز Performance فقط با اندازه‌گیری و Plan داده می‌شود، نه صرف وجود Index.
