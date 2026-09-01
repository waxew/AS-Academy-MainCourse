# Web
LocalStorage string-based، وابسته به origin و synchronous است؛ برای داده زیاد مناسب نیست. SessionStorage عمر کوتاه‌تری وابسته به session/tab دارد.

IndexedDB دیتابیس asynchronous و transactional مرورگر است: Database، Object Store، Key، Index، Transaction، Cursor و Version Upgrade. برای داده پیچیده و Blob از Web Storage مناسب‌تر است.

Service Worker درخواست‌ها را intercept می‌کند و Cache API asset/response شبکه را نگه می‌دارد؛ IndexedDB برای داده دامنه است. این دو جایگزین هم نیستند.

مرورگر سهمیه Storage دارد و ممکن است در فشار فضا داده را پاک کند؛ داده حیاتی باید export یا server sync داشته باشد.

پروژه: Note Manager با theme در LocalStorage، draft در SessionStorage، note و attachment در IndexedDB و assetها در Cache API؛ سپس migration از v1 به v2.
