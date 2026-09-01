# 07 — Partitioning و Sharding

Partitioning تقسیم منطقی یک جدول داخل یک سامانه دیتابیس است؛ Sharding تقسیم داده بین چند Node مستقل. این دو را یکی نگیرید.

Partitioning می‌تواند Range، List یا Hash باشد. انتخاب کلید مناسب باعث Partition Pruning، نگهداری ساده‌تر و آرشیو سریع‌تر می‌شود. Partition بیش از حد نیز metadata و planning overhead ایجاد می‌کند.

Sharding زمانی مطرح می‌شود که یک Node از نظر Storage، Throughput یا Write Capacity کافی نباشد. Shard Key باید توزیع یکنواخت، Query Locality و رشد آینده را در نظر بگیرد. کلید بد باعث Hot Shard می‌شود.

Rebalancing، Cross-Shard Join، Transaction توزیع‌شده و Global Secondary Index از پیچیدگی‌های اصلی Sharding هستند. Consistent Hashing انتقال داده هنگام اضافه/حذف Node را کاهش می‌دهد.

اصل طراحی: تا وقتی Vertical Scaling، Indexing، Partitioning، Cache و Read Replica پاسخ‌گو هستند، Sharding را زودهنگام وارد نکنید.
