# 12 — مدیریت داده در مقیاس بالا و Capstone

معماری مقیاس‌بالا از ترکیب اجزای درست ساخته می‌شود، نه از بیشترین تعداد فناوری. ابتدا SLO، حجم داده، نرخ ورود، الگوی Query، consistency موردنیاز، بودجه و مهارت تیم را مشخص کنید.

برای OLTP معمولاً اول Indexing، Query Tuning، Connection Pooling، Cache، Partitioning و Read Replica را بهینه کنید. سپس در صورت عبور از ظرفیت یک Node به Sharding یا دیتابیس توزیع‌شده فکر کنید.

برای Analytics، جداسازی workload عملیاتی از تحلیلی مهم است. CDC یا Pipeline داده را از OLTP به Lake/Warehouse منتقل می‌کند تا Queryهای سنگین روی دیتابیس تراکنشی اجرا نشوند.

Capstone پیشنهادی: سامانه تجارت الکترونیک با PostgreSQL Primary/Replica، Backup+PITR، PgBouncer، Monitoring، CDC به Kafka، ذخیره Bronze در Object Storage، پردازش Silver، بارگذاری Gold در Warehouse و داشبورد BI. برای هر جزء RPO/RTO، failure mode، scaling strategy و runbook تعریف کنید.
