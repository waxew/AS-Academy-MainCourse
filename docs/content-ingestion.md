# Content Ingestion Workflow

این سند روال ورود جزوه‌ها، منابع اینترنتی و محتوای جدید به MainCourse را مشخص می‌کند.

## اصل اول: عدم تکرار

قبل از ایجاد Lesson جدید، عنوان، هدف آموزشی، keywords و concepts با درس‌های موجود مقایسه می‌شوند.

- اگر concept قبلاً وجود دارد: همان Lesson عمیق‌تر می‌شود.
- اگر موضوع زیرمجموعه یک Lesson است: block/section جدید به همان Lesson اضافه می‌شود.
- اگر موضوع مستقل است: Lesson جدید با Stable ID جدید ساخته می‌شود.
- متن یکسان یا paraphrase تکراری نباید وارد Course Package شود.

## مراحل

1. جمع‌آوری منبع و ثبت attribution/reference.
2. استخراج conceptها، مثال‌ها، تمرین‌ها و خطاهای رایج.
3. مقایسه با Course Package موجود.
4. طبقه‌بندی در Foundation / Beginner / Advanced / Specialist.
5. تبدیل به Lesson Blockهای استاندارد Core.
6. افزودن Exercise/Quiz/Project فقط در صورت پوشش مهارت جدید.
7. validation ارجاعات و Stable IDها.
8. build و smoke test اپ مصرف‌کننده.

## Kotlin 2026 expansion backlog

موارد استخراج‌شده از جزوه فارسی توسعه‌یافته که باید در package Kotlin audit/merge شوند:

- Android XML/View System, Fragment, RecyclerView/DiffUtil
- DataStore و migration تنظیمات
- Activity Result, Deep Link, Permission, Camera/Photo Picker
- Notification, WorkManager, Foreground Service
- Hilt/Dagger, Koin, KSP
- Paging 3, Coil/Glide
- Compose Effects, Animation, Gesture, Canvas, Adaptive UI
- WebSocket و Ktor Client پیشرفته
- kotlinx.serialization پیشرفته
- SQLDelight و Exposed
- Spring Boot/Ktor production
- KMP iOS interop
- Android build/release engineering و profiler/debugging
- RxJava migration و XML/Compose interoperability
- TCP/UDP socket programming

این فهرست به معنی ایجاد خودکار درس جدید برای همه موارد نیست؛ هر مورد ابتدا deduplicate می‌شود.
