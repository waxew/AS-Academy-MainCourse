# Course Contract Migration

MainCourse در دوره گذار شامل دو نوع Course package است:

1. **Canonical Core-contract package** — `manifest.json` دارای `courseId` و `contentSchemaVersion` است و باید با Validator رسمی `AS-Academy-Core` بدون خطا معتبر باشد.
2. **Legacy package** — Manifest قدیمی قبل از قرارداد Core است (برای مثال دارای `id`، `direction` یا metadata نمایشی مستقیم). این package فقط برای migration نگه داشته می‌شود و نباید به‌عنوان Runtime Content Channel جدید منتشر شود.

## قانون CI

Workflow سراسری همه پوشه‌های `courses/<id>/course` را پیدا می‌کند. Canonical packageها hard-fail validation دارند. Legacy packageها با warning و شمارش migration debt گزارش می‌شوند تا وجودشان پنهان نشود.

## تعریف Done برای مهاجرت هر Course

- `id` به `courseId` تبدیل شده باشد.
- `titleFa` و `titleEn` هر دو وجود داشته باشند.
- `contentSchemaVersion` برابر schema پشتیبانی‌شده Core باشد.
- `minimumCoreVersion` کمترین نسخه واقعی لازم برای همان Course باشد.
- `rtl`, `defaultLocale`, `supportedLocales` و `capabilities` مطابق قرارداد Core تعریف شده باشند.
- فایل‌های levels/chapters/lessons/exercises/quizzes/projects با Stable IDها معتبر باشند.
- `:tools:run --args="validate ..."` موفق شود.
- پس از Compile، package تولیدی فقط خروجی build باشد و مستقیم ویرایش نشود.

## ترتیب مهاجرت

Courseهایی که در Viewer یا Runtime channel فعال‌اند اولویت بالاتر دارند. `basic` مرجع canonical فعلی است. هر Course پس از مهاجرت از لیست warningهای CI خارج می‌شود؛ هیچ bypass دائمی برای Validator مجاز نیست.
