# سطح مبانی CSS

## CSS چیست؟
CSS مخفف Cascading Style Sheets است و وظیفه کنترل ظاهر و چیدمان اسناد وب را دارد. HTML ساختار و معنای محتوا را مشخص می‌کند و CSS نحوه نمایش آن ساختار را کنترل می‌کند؛ از رنگ و فونت تا فاصله‌گذاری، چیدمان چندستونه، واکنش‌گرایی و انیمیشن.

## اولین قانون CSS
یک قانون CSS معمولاً از selector و declaration block تشکیل می‌شود. Selector مشخص می‌کند چه عنصرهایی هدف هستند و هر declaration شامل property و value است.

```css
.card {
  padding: 1rem;
  border-radius: 0.75rem;
}
```

در مثال بالا `.card` selector است. `padding` و `border-radius` property و مقادیر سمت راست value هستند.

## روش اتصال CSS
Inline برای تغییر محدود روی همان element، Internal با `<style>` برای یک سند، و External stylesheet برای پروژه واقعی. در پروژه‌های قابل نگهداری، فایل خارجی معمولاً انتخاب اصلی است چون جداسازی مسئولیت و cache مرورگر را بهتر می‌کند.

## Cascade، Inheritance و Specificity
وقتی چند قانون روی یک property اثر می‌گذارند، مرورگر با الگوریتم cascade برنده را تعیین می‌کند. origin، importance، cascade layer، specificity و ترتیب تعریف از عوامل مهم‌اند. Inheritance نیز باعث می‌شود برخی propertyها مانند بسیاری از ویژگی‌های متن از والد به فرزند منتقل شوند. استفاده بی‌رویه از `!important` نگهداری را دشوار می‌کند.

## Box Model
هر عنصر را می‌توان به یک جعبه شامل content، padding، border و margin تصور کرد. با `box-sizing: border-box` محاسبه عرض و ارتفاع در طراحی رابط معمولاً قابل پیش‌بینی‌تر می‌شود.

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

## واحدها
`px` واحد مطلق رایج است. `%` نسبت به context محاسبه می‌شود. `em` معمولاً نسبت به اندازه فونت context و `rem` نسبت به root است. واحدهای viewport مانند `vw` و `vh` برای اندازه‌های وابسته به viewport کاربرد دارند. انتخاب واحد باید متناسب با هدف responsive و accessibility باشد.

## رنگ، تایپوگرافی و فاصله‌گذاری
CSS از روش‌هایی مانند HEX، rgb() و hsl() برای رنگ پشتیبانی می‌کند. در تایپوگرافی باید font-family، font-size، line-height، weight و خوانایی متن را همزمان در نظر گرفت. برای رابط فارسی، فونت مناسب، line-height کافی و آزمایش RTL ضروری است.

## تمرین
یک کارت معرفی بسازید که عنوان، توضیح و دکمه داشته باشد. بدون Inline CSS، padding، border، radius، background، typography و فاصله بین اجزا را تنظیم کنید. سپس `box-sizing` را حذف و تفاوت محاسبه ابعاد را بررسی کنید.

## خطاهای رایج
فراموش کردن `;` یا `}`، اشتباه در مسیر stylesheet، استفاده نابجا از id برای styling، وابستگی زیاد به `!important`، و تعیین width ثابت برای تمام نمایشگرها از خطاهای متداول شروع CSS هستند.

## ارزیابی
دانشجو پس از این بخش باید بتواند stylesheet را متصل کند، syntax را بخواند، selector ساده بنویسد، Box Model را توضیح دهد و یک کامپوننت ساده را بدون شکستن ساختار HTML استایل‌دهی کند.
