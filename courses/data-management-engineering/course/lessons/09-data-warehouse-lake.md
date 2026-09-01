# 09 — Data Warehouse، Data Lake و Lakehouse

Data Warehouse برای تحلیل ساخت‌یافته، مدل‌سازی و Queryهای BI طراحی می‌شود؛ Data Lake داده خام و نیمه‌ساخت‌یافته را با هزینه کمتر نگه می‌دارد؛ Lakehouse تلاش می‌کند انعطاف Lake را با قابلیت‌های مدیریتی Warehouse ترکیب کند.

در Dimensional Modeling معمولاً Fact و Dimension داریم. Star Schema ساده‌تر و سریع‌تر برای BI است؛ Snowflake بخشی از Dimensionها را نرمال می‌کند. Slowly Changing Dimension برای نگهداری تغییرات ویژگی Dimension استفاده می‌شود؛ Type 1 مقدار قبلی را جایگزین و Type 2 تاریخچه را با رکورد جدید نگه می‌دارد.

معماری Medallion داده را به Bronze (خام)، Silver (پاک‌سازی و استاندارد) و Gold (آماده مصرف تحلیلی) تقسیم می‌کند. این تفکیک Debugging، Lineage و کیفیت داده را بهتر می‌کند.

Data Governance شامل Catalog، Lineage، Ownership، Classification، Retention و Data Quality است.
