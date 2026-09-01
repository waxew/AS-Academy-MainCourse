# AS Academy MainCourse

`AS-Academy-MainCourse` منبع واحد (Single Source of Truth) برای تمام محتوای آموزشی AS Academy است.

## مسئولیت

این ریپو فقط داده و محتوای دوره‌ها و خروجی‌های انتشار محتوایی آن‌ها را مدیریت می‌کند:

- سطوح: مبانی، مقدماتی، پیشرفته، تخصصی
- فصل‌ها و درس‌ها
- مثال‌ها و Code Blockها
- تمرین‌ها و Acceptance Criteria
- Quizها و آزمون‌ها
- پروژه‌ها و Capstone
- Solution/Rubric
- Glossary
- Course assets و metadata
- Branding/Capability metadata مربوط به هر Course
- ساخت Package کامپایل‌شده قابل مصرف توسط Android Host
- انتشار Metadata و Package برای Runtime Content Update مستقل از APK

منطق Android، Navigation، Database، Progress، Search، Quiz Engine و سایر قابلیت‌های مشترک در `AS-Academy-Core` قرار دارند.
پوسته و Design System مشترک در `AS-Academy-MainUi` قرار می‌گیرد.

## ساختار استاندارد

```text
courses/
  kotlin/
    course/
      manifest.json
      course.json
      levels.json
      chapters.json
      lessons/
      exercises/
      quizzes/
      projects/
      solutions/
      glossary/
      assets/
      branding/
```

هر Course باید چهار سطح اصلی `foundation`, `beginner`, `advanced`, `specialist` را با Stable IDهای خودش نگه دارد.

## دو خروجی از یک منبع واحد

یک Course Package فقط یک منبع قابل ویرایش در `courses/<course-id>/course` دارد، اما از همان منبع دو نوع خروجی تولید می‌شود:

1. **Bundled Content** — هنگام Build اپ، Package با Compiler رسمی Core به JSON واحد تبدیل و داخل APK قرار می‌گیرد. این نسخه fallback آفلاین همیشگی برنامه است.
2. **Runtime Content Channel** — همان Package معتبر به فایل قابل دانلود تبدیل و همراه Metadata شامل نسخه، `minimumCoreVersion` و SHA-256 منتشر می‌شود. اپ می‌تواند آن را بدون انتشار APK جدید دریافت کند.

```text
courses/<id>/course
        |
        +--> Core Validate + Compile --> APK asset
        |
        +--> Core Validate + Compile --> content release channel
                                      |-- latest.json
                                      `-- <course>-course.json
```

Course App هیچ‌وقت محتوای اصلی را در Repository خودش Fork نمی‌کند. Asset داخل APK نیز خروجی Build از MainCourse است، نه نسخه دوم قابل ویرایش.

## قرارداد Runtime Content Update

فایل `latest.json` هر کانال باید حداقل این فیلدها را داشته باشد:

```json
{
  "courseId": "basic",
  "version": "1.1.0",
  "minimumCoreVersion": "1.3.0",
  "sha256": "<64-hex-sha256>",
  "downloadUrl": "https://.../basic-course.json"
}
```

قواعد انتشار:

- Source قبل از Compile باید با Validator رسمی `AS-Academy-Core` معتبر باشد.
- SHA-256 باید از دقیقاً همان فایل Package منتشرشده محاسبه شود.
- `courseId`، `version` و `minimumCoreVersion` از `course/manifest.json` گرفته می‌شوند.
- هر تغییر محتوایی که باید به کاربران موجود برسد باید `manifest.version` را افزایش دهد؛ در غیر این صورت Runtime Updater آن را همان نسخه فعلی تشخیص می‌دهد.
- Stable ID درس، آزمون، تمرین و پروژه بعد از انتشار نباید بدون Migration شکسته شود تا Progress و History کاربر حفظ شود.
- Release asset خروجی Build است؛ ویرایش مستقیم آن ممنوع است. اصلاح محتوا همیشه از `courses/<id>/course` شروع می‌شود.

## کانال Basic

Basic اولین Course متصل به Runtime Content Update است. Workflow اختصاصی آن Package را از `courses/basic/course` Validate و Compile می‌کند و یک کانال Rolling با نام `basic-content` می‌سازد.

آدرس‌های پایدار مصرف Runtime:

```text
Metadata:
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/latest.json

Package:
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/basic-course.json
```

جزئیات خود Course در [`courses/basic/README.md`](courses/basic/README.md) ثبت شده است.

## Kotlin migration

محتوای موجود `AS-Academy-Kotlin/course` به `courses/kotlin/course` منتقل می‌شود و پس از تثبیت مهاجرت، تغییرات جدید محتوا فقط در MainCourse انجام خواهند شد.

Course appها حق ندارند منطق یا محتوای اصلی دوره را به‌صورت مستقل fork کنند؛ App باید Course Package را از MainCourse دریافت/بسته‌بندی کند و در صورت فعال بودن کانال Runtime، نسخه جدیدتر را نیز از همان منبع رسمی دریافت کند.
