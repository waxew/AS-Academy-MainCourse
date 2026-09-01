# 11 — Apache Kafka و پردازش بلادرنگ

Kafka یک پلتفرم Event Streaming توزیع‌شده است. داده در Topic قرار می‌گیرد و Topic به Partition تقسیم می‌شود. ترتیب فقط داخل هر Partition تضمین می‌شود.

Producer پیام را منتشر می‌کند؛ Consumer پیام را می‌خواند؛ Consumer Group باعث می‌شود Partitionها بین Consumerهای یک گروه تقسیم شوند. Offset موقعیت خواندن Consumer را نشان می‌دهد.

Replication Factor تحمل خرابی Broker را بالا می‌برد. Leader هر Partition درخواست‌ها را مدیریت و Replicaها آن را دنبال می‌کنند. انتخاب تعداد Partition مستقیماً بر Parallelism و هزینه عملیاتی اثر دارد.

Delivery Semantics: at-most-once ممکن است داده از دست بدهد، at-least-once ممکن است تکرار ایجاد کند، exactly-once نیازمند طراحی و پشتیبانی مناسب در کل Pipeline است. در عمل Idempotency و Deduplication بسیار مهم‌اند.

در Stream Processing مفاهیم Event Time، Processing Time، Window، Watermark و Late Event تعیین‌کننده‌اند. Backpressure زمانی رخ می‌دهد که مصرف‌کننده از نرخ ورود عقب بماند.
