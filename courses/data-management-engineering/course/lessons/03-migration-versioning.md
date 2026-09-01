# 03 — Migration و Versioning

Schema مانند کد باید Version شود. هر تغییر ساختار باید قابل تکرار، قابل ممیزی و در صورت امکان قابل بازگشت باشد.

Migrationها معمولاً به‌صورت فایل‌های شماره‌دار یا timestampدار نگهداری می‌شوند. ابزارهایی مثل Flyway و Liquibase تاریخچه Migration را در خود دیتابیس ثبت می‌کنند. اصل مهم این است که محیط Development، Staging و Production مسیر یکسانی را طی کنند.

تغییرات خطرناک: Rename/Drop Column، تغییر نوع داده، افزودن Constraint سنگین و ساخت Index روی جدول بزرگ. برای Zero-Downtime از الگوی Expand/Contract استفاده کنید: ابتدا ساختار جدید را اضافه کنید، اپلیکیشن را سازگار کنید، داده را Backfill کنید، سپس ساختار قدیمی را حذف کنید.

برای Migration بزرگ باید Lock Duration، حجم WAL/Redo، Replication Lag، Rollback Plan و Compatibility نسخه‌های قدیم/جدید برنامه بررسی شود.

تمرین: ستونی به نام `full_name` دارید و می‌خواهید آن را به `first_name` و `last_name` تبدیل کنید بدون توقف سرویس. مراحل Expand/Contract را طراحی کنید.
