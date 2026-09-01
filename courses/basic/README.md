# Basic — Programming Foundations

`courses/basic/course` منبع رسمی و یکتای محتوای آموزشی AS Academy Basic است.

## وضعیت مهاجرت

مهاجرت اولیه از `waxew/AS-Academy-Basic/course/basic` انجام و بسته کامل با Validator رسمی `AS-Academy-Core` بررسی شده است. کپی محلی Course Package از خط توسعه جدید Basic حذف شده و از این پس هیچ تغییر آموزشی نباید ابتدا در Application Repository انجام شود.

## وضعیت محتوای منتقل‌شده

- 4 سطح: مبانی، مقدماتی، پیشرفته، تخصصی/بازار کار
- 39 فصل
- 157 درس
- 73 Quiz
- 534 سؤال
- 195 Exercise
- 40 Challenge Exercise
- 14 Project
- 69 Glossary Entry
- Placement Test، Depth Assessment، Micro Quiz و Interview Assessment
- Final Capstone: `basic-prj-014`

## محل ویرایش

تمام تغییرات جدید از همین مسیرها انجام می‌شوند:

- `course/manifest.json` — نسخه و هویت Course Package
- `course/levels.json` — سطح‌ها
- `course/chapters.json` — فصل‌ها و سرفصل‌ها
- `course/lessons/` — درس‌ها
- `course/quizzes/` — کویزها و آزمون‌ها
- `course/exercises/` — تمرین‌ها و Challengeها
- `course/projects/` — پروژه‌ها و Capstone
- `course/glossary/` — واژه‌نامه و داده مرور
- `course/references.json` — منابع
- `course/assets.json` — متادیتای منابع رسانه‌ای
- `course/branding.json` — متادیتای برند دوره؛ UI اجرایی در MainUi قرار دارد

## جریان Build داخل APK

```text
Edit in MainCourse
  -> Core Validate
  -> Core Compile
  -> AS-Academy-Basic/app/src/main/assets/basic-course.json
  -> Core Runtime Loader
  -> MainUi
  -> درس / Quiz / Exercise / Project داخل برنامه
```

Basic هنگام CI/build همین بسته را دریافت و به `basic-course.json` تبدیل می‌کند. اگر MainCourse یا Course Package اصلی موجود نباشد، آماده‌سازی Build باید fail شود. Asset داخل APK یک خروجی تولیدشده از MainCourse و fallback آفلاین برنامه است؛ نسخه قابل ویرایش دوم محسوب نمی‌شود.

## Runtime Content Update بدون APK جدید

علاوه بر Asset داخل APK، MainCourse برای Basic یک کانال انتشار مستقل Content دارد. Workflow انتشار پس از Validate و Compile این سه فایل را در GitHub Release با tag ثابت `basic-content` منتشر می‌کند:

```text
latest.json
basic-course.json
basic-course.json.sha256
```

آدرس‌های پایدار:

```text
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/latest.json
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/basic-course.json
```

`latest.json` شامل `courseId`، نسخه محتوا، حداقل نسخه Core، SHA-256 فایل Package و URL دانلود است. Android Host ابتدا جدیدترین محتوای معتبر محلی را نمایش می‌دهد و سپس کانال را بررسی می‌کند؛ بنابراین اتصال شبکه مانع باز شدن آموزش‌ها نمی‌شود.

جریان Runtime:

```text
Basic launches
  -> CourseContentStore
     -> validate bundled basic-course.json from APK
     -> validate installed runtime course-package.json when present
     -> compare SemVer
        -> installed wins only when strictly newer than bundled
        -> bundled wins when equal/newer or installed is invalid
  -> UI becomes usable
  -> HTTPS latest.json check
  -> metadata SemVer/minimumCoreVersion preflight
     -> current/downgrade/incompatible: no Package download
     -> newer/installable: download candidate
  -> SHA-256 + Course Validator + courseId + SemVer + minimumCoreVersion re-check
  -> atomic install + rollback backup
  -> reload CourseBundle
  -> MainUi shows new content
```

این سیاست دو نوع Update را با هم سازگار می‌کند. اگر Runtime Content مثلاً `1.1.1` نصب شده باشد و APK بعدی Course `1.2.0` را Bundle کند، در حالت Offline هم `1.2.0` نمایش داده می‌شود و Runtime Package قدیمی روی APK جدید سایه نمی‌اندازد. اگر Runtime Package واقعاً از Asset APK جدیدتر باشد، همان Runtime Package فعال می‌ماند.

اگر اینترنت قطع باشد، Metadata خراب باشد، فایل دانلود ناقص باشد، SHA-256 تطبیق نکند، Course نامعتبر باشد یا نسخه به Core جدیدتری نیاز داشته باشد، نسخه معتبر محلی فعلی فعال باقی می‌ماند. اگر فایل نصب‌شده خراب شود Core آن را قرنطینه می‌کند؛ اگر Asset APK خراب ولی Runtime Package معتبر باشد، نسخه نصب‌شده حفظ می‌شود تا آموزش‌ها از دسترس خارج نشوند.

Progress، Quiz History، Exercise Draft، Project Progress، Flashcard Progress و Settings در دیتابیس/DataStore برنامه نگهداری می‌شوند و با تعویض Course Package حذف نمی‌شوند.

## قانون افزایش نسخه محتوا

برای هر تغییر آموزشی که باید از Runtime Channel به کاربران موجود برسد، مقدار `version` در `course/manifest.json` باید افزایش یابد. مثال:

```text
1.1.0 -> 1.1.1
```

افزایش نسخه APK لازم نیست، مگر اینکه خود Runtime، UI، Core/API، Permission یا قابلیت native برنامه تغییر کرده باشد.

## مالکیت اجزا

- محتوای آموزشی: `AS-Academy-MainCourse/courses/basic/course`
- Validator/Compiler/Updater/Storage/Rollback: `AS-Academy-Core`
- نمایش Lesson/Quiz/Exercise/Project: `AS-Academy-MainUi`
- Android package، signing، versionCode و اتصال Course: `AS-Academy-Basic`
