# AS Academy MainCourse

`AS-Academy-MainCourse` منبع واحد (Single Source of Truth) برای تمام محتوای آموزشی AS Academy است.

## مسئولیت

این ریپو فقط داده و محتوای دوره‌ها را نگه می‌دارد:

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

## Kotlin migration

محتوای موجود `AS-Academy-Kotlin/course` به `courses/kotlin/course` منتقل می‌شود و پس از تثبیت مهاجرت، تغییرات جدید محتوا فقط در MainCourse انجام خواهند شد.

Course appها حق ندارند منطق یا محتوای اصلی دوره را به‌صورت مستقل fork کنند؛ app باید Course Package را از MainCourse دریافت/بسته‌بندی کند.
