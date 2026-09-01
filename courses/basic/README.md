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

علاوه بر Asset داخل APK، MainCourse برای Basic یک کانال انتشار مستقل Content دارد. Workflow انتشار پس از Validate و Compile این دو فایل را در GitHub Release با tag ثابت `basic-content` منتشر می‌کند:

```text
latest.json
basic-course.json
```

آدرس‌های پایدار:

```text
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/latest.json
https://github.com/waxew/AS-Academy-MainCourse/releases/download/basic-content/basic-course.json
```

`latest.json` شامل `courseId`، نسخه محتوا، حداقل نسخه Core، SHA-256 فایل Package و URL دانلود است. Android Host ابتدا محتوای موجود روی دستگاه را نمایش می‌دهد و سپس کانال را بررسی می‌کند؛ بنابراین اتصال شبکه مانع باز شدن آموزش‌ها نمی‌شود.

جریان Runtime:

```text
Basic launches
  -> CourseContentStore
     -> installed valid course-package.json ? use it
     -> otherwise use bundled basic-course.json from APK
  -> UI becomes usable
  -> HTTPS latest.json check
  -> download candidate when newer
  -> SHA-256 + Course Validator + courseId + SemVer + minimumCoreVersion
  -> atomic install + rollback backup
  -> reload CourseBundle
  -> MainUi shows new content
```

اگر اینترنت قطع باشد، Metadata خراب باشد، فایل دانلود ناقص باشد، SHA-256 تطبیق نکند، Course نامعتبر باشد یا نسخه به Core جدیدتری نیاز داشته باشد، نسخه فعلی فعال باقی می‌ماند. اگر فایل نصب‌شده بعداً خراب شود، Core آن را از مسیر فعال خارج می‌کند و Asset داخل APK را به‌عنوان fallback آفلاین نمایش می‌دهد.

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
