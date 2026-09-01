# Offline-First و Sync
UI باید از داده محلی پایدار تغذیه شود و شبکه نقش refresh/sync داشته باشد.

Write ابتدا local ثبت و سپس Outbox ساخته می‌شود. وضعیت‌های PENDING، SYNCING، SYNCED، FAILED و CONFLICTED مفیدند. WorkManager برای sync پایدار Android با constraint و retry مناسب است.

Read می‌تواند Stale-While-Revalidate باشد: داده محلی فوراً نمایش داده، شبکه refresh و نتیجه در DB نوشته شود.

Delta Sync با cursor/revision فقط تغییرات را می‌گیرد. حذف با tombstone/change-log منتقل می‌شود. Retry باید idempotent باشد؛ UUID یا idempotency key مانع عملیات تکراری می‌شود.

Conflict policy می‌تواند Server-Wins، Client-Wins، Last-Write-Wins، Merge یا Manual باشد و باید per-entity انتخاب شود.

تست: airplane mode، قطع شبکه وسط sync، process death، دو device همزمان، delete-vs-update، migration همراه pending sync و request تکراری.
