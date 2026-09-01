# CSS، Layout و Responsive Design

## CSS چگونه تصمیم می‌گیرد؟
برای فهم CSS باید سه مفهوم Cascade، Specificity و Inheritance را جدی گرفت. بسیاری از مشکلات ظاهری پروژه در واقع مشکل «اولویت قوانین» هستند نه مشکل مرورگر.

## Box Model
هر Element را می‌توان به چهار ناحیه Content، Padding، Border و Margin تحلیل کرد. استفاده عمومی از `box-sizing: border-box` محاسبه ابعاد را قابل پیش‌بینی‌تر می‌کند.

```css
*, *::before, *::after { box-sizing: border-box; }
```

## Flexbox
برای چیدمان یک‌بعدی مناسب است. محور اصلی با `flex-direction` و توزیع روی آن با `justify-content` کنترل می‌شود؛ `align-items` محور متقاطع را کنترل می‌کند.

## Grid
برای layout دوبعدی و ساختارهای سطری/ستونی قدرتمند است.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: 1rem;
}
```

این الگو بدون تعیین تعداد ثابت ستون، کارت‌ها را متناسب با فضای موجود بازچینی می‌کند.

## Responsive و Mobile First
Responsive Design یعنی طراحی بتواند با اندازه صفحه، قابلیت ورودی و فضای در دسترس سازگار شود. Mobile First معمولاً با Style پایه برای viewport کوچک و افزودن قابلیت در breakpointهای بزرگ‌تر پیاده می‌شود.

```css
.page { padding: 1rem; }
@media (min-width: 48rem) {
  .page { padding: 2rem; }
}
```

## Container Query
در طراحی کامپوننتی، گاهی اندازه container مهم‌تر از viewport است. Container Query اجازه می‌دهد Component بر اساس فضای والد خود واکنش نشان دهد.

## Animation
Animation باید هدف داشته باشد و نباید خوانایی یا دسترس‌پذیری را کاهش دهد. ترجیح `prefers-reduced-motion` کاربر باید رعایت شود.

## Sass، Bootstrap و Tailwind
Sass امکاناتی برای سازمان‌دهی و تولید CSS فراهم می‌کند. Bootstrap مجموعه Component/Utility آماده است. Tailwind رویکرد Utility-first دارد. هنرجو باید قبل از این ابزارها CSS را بفهمد تا Framework تبدیل به وابستگی بدون درک نشود.

## تمرین
یک Dashboard با Sidebar، Header، Card Grid و Table بسازید که از موبایل تا Desktop قابل استفاده باشد. سپس نسخه‌ای با CSS خام و نسخه‌ای با Tailwind یا Bootstrap مقایسه کنید.
