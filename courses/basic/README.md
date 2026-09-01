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

## جریان انتشار محتوا

`Edit in MainCourse -> Core Validate -> Core Compile -> MainUi/Core runtime -> Basic Android Host`

Basic هنگام CI/build همین بسته را دریافت و به `basic-course.json` تبدیل می‌کند. اگر MainCourse یا این Course Package موجود نباشد، آماده‌سازی محتوا باید fail شود؛ fallback یا کپی دوم داخل Host مجاز نیست.
