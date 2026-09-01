# Kotlin content expansion plan

این سند صف مهاجرت محتوای جزوه توسعه‌یافته Kotlin به MainCourse است. اصل قطعی: Stable IDهای منتشرشده تغییر نمی‌کنند و هیچ درس تکراری ایجاد نمی‌شود.

## ادغام در درس‌های موجود

موضوعاتی که مفهوم پایه آن‌ها از قبل وجود دارد، به همان Lesson موجود افزوده می‌شوند:

- Coroutines / Flow / Channels / Mutex / Testing
- Generics / Variance / Sealed / Inline / Reified / Reflection
- Compose fundamentals / architecture / state
- Room / Offline-first / Sync
- Ktor backend / persistence / auth / resilience / observability
- KMP / Compose Multiplatform / target strategy
- Security / CI-CD / Release Engineering

## Candidate lessonهای جدید

فقط در صورت نبود پوشش مستقل در Course فعلی Stable ID جدید دریافت می‌کنند:

- Android View System: XML, Fragment, RecyclerView, DiffUtil
- DataStore
- Activity Result API, Deep Link و Navigation integration
- Runtime Permissions, Camera و Photo Picker
- Notification, WorkManager و Foreground Service
- Hilt/Dagger و Koin
- KSP و code generation
- Paging 3
- Coil/Glide و image pipeline
- Compose Side Effects
- Compose Animation/Gesture/Canvas
- Adaptive UI
- WebSocket و realtime client/server
- Ktor Client پیشرفته
- kotlinx.serialization پیشرفته
- SQLDelight و Exposed
- Spring Boot production with Kotlin
- KMP iOS interop
- Android Build Engineering
- Android publishing/signing/release
- Debugging/Profiler/ANR/Memory
- RxJava to Coroutines/Flow migration
- XML/Compose interoperability
- TCP/UDP socket programming

## Definition of Done برای هر Lesson جدید

هر درس باید شامل هدف، پیش‌نیاز، توضیح مفهومی، مثال معتبر، خطاهای رایج، Best Practice، تمرین مرتبط، Quiz/assessment mapping و reference metadata باشد. درس تخصصی بدون سناریوی production کامل محسوب نمی‌شود.
