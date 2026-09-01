# فصل ۱ — مبانی Frontend و محیط توسعه

## هدف
در پایان این فصل هنرجو می‌داند کد Frontend کجا اجرا می‌شود، Browser چگونه HTML/CSS/JavaScript را پردازش می‌کند و چگونه یک محیط توسعه استاندارد بسازد.

## Frontend چیست؟
Frontend بخش قابل مشاهده و تعاملی یک محصول وب است که در مرورگر اجرا می‌شود. HTML ساختار و معنا، CSS ارائه بصری و JavaScript رفتار و تعامل را تعریف می‌کند. Frontend فقط «ظاهر سایت» نیست؛ دسترس‌پذیری، کارایی، مدیریت وضعیت، ارتباط با API، امنیت سمت کاربر، سازگاری مرورگر و تجربه کاربری نیز بخشی از مسئولیت آن است.

## چرخه ساده بارگذاری صفحه
1. کاربر URL را وارد می‌کند.
2. مرورگر منبع HTML را دریافت می‌کند.
3. HTML به DOM تبدیل می‌شود.
4. CSS دریافت و تحلیل می‌شود.
5. مرورگر اطلاعات ساختار و Style را برای Layout/Paint استفاده می‌کند.
6. JavaScript می‌تواند DOM، Style و رفتار صفحه را تغییر دهد.

## ابزارها
- VS Code یا ویرایشگر مناسب
- مرورگر مدرن
- DevTools: Elements، Console، Network، Sources، Application و Performance
- Git برای تاریخچه تغییرات
- Node.js/npm برای ابزارهای Build و Packageها

## اولین پروژه
```text
frontend-start/
  index.html
  css/style.css
  js/app.js
  assets/
```

## خطاهای رایج
- اشتباه گرفتن JavaScript مرورگر با Node.js
- نصب Package بدون فهم dependency
- نادیده گرفتن Console و Network هنگام Debug
- شروع Framework قبل از تسلط نسبی به HTML/CSS/JavaScript

## تمرین
یک پوشه پروژه بسازید، HTML/CSS/JS را به هم متصل کنید، در Console یک پیام چاپ کنید و درخواست‌های صفحه را در Network بررسی کنید.

## Quiz
1. DOM چیست؟
2. وظیفه CSS چیست؟
3. Network panel چه کمکی می‌کند؟
4. npm چه نقشی در پروژه Frontend دارد؟

---

# فصل ۲ — HTML از پایه تا Semantic

HTML زبان نشانه‌گذاری وب است و هدف اصلی آن تعریف ساختار و معنای محتواست.

## اسکلت استاندارد
```html
<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>اولین صفحه</title>
</head>
<body>
  <main>
    <h1>آموزش Frontend</h1>
    <p>اولین صفحه معنایی ما.</p>
  </main>
</body>
</html>
```

## Semantic HTML
به‌جای استفاده بی‌هدف از `div`، در جای مناسب از `header`، `nav`، `main`، `section`، `article`، `aside` و `footer` استفاده می‌کنیم. Semantic HTML فهم ساختار را برای توسعه‌دهنده، موتور جست‌وجو و فناوری‌های کمکی بهتر می‌کند.

## فرم استاندارد
هر ورودی باید تا حد ممکن label واضح، نوع مناسب و قواعد Validation مشخص داشته باشد.

```html
<form>
  <label for="email">ایمیل</label>
  <input id="email" name="email" type="email" required autocomplete="email">
  <button type="submit">ارسال</button>
</form>
```

## رسانه
برای تصویر responsive باید با مفاهیم `srcset`، `sizes` و `picture` آشنا شد. برای ویدئو و صوت نیز باید fallback و accessibility در نظر گرفته شود.

## تمرین فصل
صفحه مقاله‌ای بسازید که header، navigation، main/article، تصویر، جدول اطلاعات، فرم دیدگاه و footer داشته باشد و بدون CSS نیز ساختار آن قابل فهم باشد.
