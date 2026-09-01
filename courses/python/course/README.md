# Python Course Package

این پوشه ورودی مستقیم Content Engine در `AS-Academy-Core` است.

Core مدل‌های `CourseManifest`, `CourseLevel`, `Chapter`, `Lesson` و `LessonBlock` را تعریف می‌کند و این ریپو فقط داده اختصاصی Python را ارائه می‌دهد.

ترتیب بارگذاری پیشنهادی:
1. `manifest.json`
2. `levels.json`
3. `chapters.json`
4. همه فایل‌های `lessons/*.json`

نوع blockها دقیقاً مطابق Lesson Renderer مرکزی هستند: TITLE، PARAGRAPH، LIST، TABLE، CODE، OUTPUT، TIP، WARNING، NOTE، IMPORTANT، EXERCISE، QUIZ، PROJECT، DIAGRAM و REFERENCE.
