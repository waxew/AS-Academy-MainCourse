# 05 — Connection Pooling

ساخت Connection دیتابیس هزینه دارد: احراز هویت، تخصیص حافظه، Session State و منابع شبکه. اگر هر Request یک Connection جدید بسازد، تحت بار بالا دیتابیس قبل از مصرف CPU مفید با کمبود Connection مواجه می‌شود.

Connection Pool تعدادی اتصال آماده نگه می‌دارد و بین درخواست‌ها بازاستفاده می‌کند. پارامترهای مهم: min/max pool size، timeout، idle timeout، max lifetime و validation.

در PostgreSQL ابزارهایی مانند PgBouncer رایج‌اند. Session Pooling یک Connection سرور را تا پایان Session به Client می‌دهد؛ Transaction Pooling بعد از هر Transaction آن را آزاد می‌کند و مقیاس‌پذیرتر است اما برخی قابلیت‌های Session-level را محدود می‌کند.

قاعده ظرفیت: اندازه Pool را با تعداد instanceهای برنامه ضرب کنید. اگر 20 instance هر کدام pool=50 داشته باشند، حداکثر 1000 Connection ممکن است ایجاد شود. عدد مناسب باید بر اساس ظرفیت دیتابیس، CPU، workload و concurrency اندازه‌گیری شود نه حدس.
