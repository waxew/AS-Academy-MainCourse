# 08 — Monitoring، Performance و Troubleshooting

مانیتورینگ خوب باید چهار حوزه را پوشش دهد: منابع سیستم، سلامت دیتابیس، رفتار Query و تجربه سرویس.

شاخص‌ها: CPU، Memory، Disk IOPS/Latency، Connection Count، Cache Hit Ratio، TPS/QPS، Lock Wait، Deadlock، Replication Lag، WAL/Binlog growth، Slow Query، Table/Index bloat و زمان Backup.

در Troubleshooting از روش مشاهده‌محور استفاده کنید: اول Symptom را دقیق تعریف کنید، سپس Time Window، Queryها، Planها، Lockها و تغییرات اخیر را بررسی کنید. `EXPLAIN` و `EXPLAIN ANALYZE` برای فهم Query Plan کلیدی هستند.

Index بیشتر همیشه بهتر نیست. Index هزینه Write، Storage و Vacuum/Maintenance را بالا می‌برد. Index باید از workload واقعی استخراج شود.

برای Incident، Timeline، Impact، Root Cause، Mitigation و Action Item ثبت کنید. Postmortem باید بدون سرزنش و با تمرکز بر اصلاح سیستم باشد.
