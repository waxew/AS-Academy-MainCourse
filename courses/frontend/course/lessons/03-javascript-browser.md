# JavaScript، DOM، Event و API

JavaScript رفتار برنامه را می‌سازد. قبل از DOM باید متغیر، نوع داده، function، array، object، scope، module و error handling فهمیده شوند.

## DOM و Event
DOM نمایش شی‌گرای Document در حافظه است. JavaScript می‌تواند nodeها را پیدا، ایجاد، حذف یا تغییر دهد. Eventها پایه تعامل هستند و مفاهیم target/currentTarget، bubbling، capturing، preventDefault و delegation باید فهمیده شوند.

```js
const button = document.querySelector('#save');
const output = document.querySelector('#status');
button.addEventListener('click', () => { output.textContent = 'ذخیره شد'; });
```

## Fetch و API
`fetch()` یک Promise برمی‌گرداند. موفق بودن transport به معنی موفق بودن HTTP status نیست و `response.ok` باید بررسی شود.

```js
async function loadUsers() {
  const response = await fetch('/api/users');
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

UI واقعی باید حالت‌های loading، empty، success و error داشته باشد. برای درخواست‌های قابل لغو می‌توان از AbortController استفاده کرد.

## تمرین
یک صفحه جست‌وجو بسازید که از API داده بگیرد، loading نمایش دهد، خطای شبکه را مدیریت کند، نتیجه خالی را نشان دهد و درخواست قبلی را هنگام جست‌وجوی جدید لغو کند.
