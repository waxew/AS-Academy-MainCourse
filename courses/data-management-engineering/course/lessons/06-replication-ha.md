# 06 — Replication و High Availability

Replication کپی تغییرات داده بین Nodeهاست؛ HA هدف بزرگ‌تر یعنی ادامه خدمت هنگام خرابی است. داشتن Replica به‌تنهایی HA کامل نیست مگر Detection، Failover، Routing و Recovery هم طراحی شده باشد.

Asynchronous Replication کم‌تاخیرتر است ولی در خرابی Primary احتمال از دست رفتن آخرین تراکنش‌ها وجود دارد. Synchronous Replication دوام بیشتری می‌دهد اما Latency نوشتن را افزایش می‌دهد.

Read Replica می‌تواند بار خواندن را توزیع کند، اما Replication Lag باعث Read-After-Write inconsistency می‌شود. برای داده حساس باید مسیر خواندن بعد از نوشتن مشخص باشد.

Failover شامل تشخیص خرابی، انتخاب Primary جدید، تغییر Route/Service Discovery و جلوگیری از Dual Primary است. Split Brain زمانی رخ می‌دهد که دو Node خود را Primary بدانند. Quorum، fencing و consensus برای جلوگیری از آن اهمیت دارند.

HA را با Fault Injection و Game Day تست کنید؛ صرفاً داشتن معماری روی کاغذ کافی نیست.
