# 10 — ETL، ELT و طراحی Data Pipeline

ETL یعنی Extract سپس Transform و بعد Load؛ ELT ابتدا داده را وارد مقصد می‌کند و Transform داخل پلتفرم تحلیلی انجام می‌شود. انتخاب بین آن‌ها به حجم، توان مقصد، Governance و نوع workload بستگی دارد.

یک Pipeline تولیدی باید Idempotent باشد: اجرای مجدد نباید داده را خراب یا چندبار ثبت کند. همچنین باید Retry، Dead Letter، Checkpoint، Backfill، Observability و Data Quality داشته باشد.

Batch برای پردازش دوره‌ای و حجم بالا مناسب است. Streaming برای latency پایین و واکنش سریع استفاده می‌شود. CDC تغییرات دیتابیس عملیاتی را از لاگ تراکنش استخراج می‌کند و به مقصدهای دیگر می‌فرستد.

Orchestration با ابزارهایی مثل Airflow وابستگی Taskها، Schedule، Retry، SLA و Backfill را مدیریت می‌کند. dbt برای Transformation مبتنی بر SQL، تست و lineage مناسب است؛ Spark برای پردازش توزیع‌شده حجم بالا کاربرد دارد.

طراحی نمونه: PostgreSQL -> CDC -> Kafka -> پردازش -> Object Storage Bronze -> Spark/dbt -> Warehouse Gold -> BI.
