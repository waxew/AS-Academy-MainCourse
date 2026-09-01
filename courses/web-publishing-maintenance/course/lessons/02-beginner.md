# سطح مقدماتی — سرور و استقرار عملی

## Linux Server
کار با pwd، ls، cd، cp، mv، rm، mkdir، cat، less، grep، find، tail و journalctl پایه مدیریت سرور است. مسیرهای /etc برای تنظیمات، /var/log برای بسیاری از Logها، /var/www برای محتوای وب در برخی الگوها و /home برای کاربران رایج‌اند.

Permissionها با owner/group/other و read/write/execute کنترل می‌شوند. از اجرای سرویس با root تا حد امکان اجتناب کنید. برای مدیریت Package از مدیر بسته توزیع مانند apt استفاده کنید و Patch امنیتی را منظم انجام دهید.

## SSH
به‌جای Password، کلید عمومی/خصوصی را ترجیح دهید. Private Key باید محرمانه بماند. ورود مستقیم root را محدود کنید، حساب مدیریتی مشخص بسازید و دسترسی‌ها را بر اساس Least Privilege بدهید.

## Process، Service و systemd
Process نمونه در حال اجرای برنامه است. systemd سرویس‌ها را start/stop/restart و در Boot فعال می‌کند. وضعیت و Log سرویس را قبل و بعد از Deploy بررسی کنید.

## Firewall
فقط Portهای لازم را باز کنید. برای وب معمولاً 80/443 و برای مدیریت SSH فقط از مبادی مورد نیاز. Firewall جایگزین امنیت برنامه نیست؛ یک لایه دفاعی است.

## Apache
مفاهیم DocumentRoot، VirtualHost، Module، Access/Error Log و Rewrite را یاد بگیرید. هر سایت می‌تواند Virtual Host مستقل داشته باشد. فایل تنظیمات را قبل از Reload اعتبارسنجی کنید.

## Nginx
Server Block، root، index، location، access_log/error_log و proxy_pass اجزای کلیدی‌اند. Nginx می‌تواند Static File Server، TLS Terminator و Reverse Proxy برای Backend باشد.

نمونه مفهومی Reverse Proxy:
```nginx
server {
    listen 443 ssl;
    server_name example.com;
    location /api/ {
        proxy_pass http://127.0.0.1:3000/;
    }
}
```
در Production باید TLS، Headerها، Timeoutها، محدودیت اندازه درخواست و Log نیز متناسب با برنامه تنظیم شوند.

## SSL/TLS و Let's Encrypt
گواهی را برای دامنه صحیح دریافت کنید، تمدید خودکار را فعال و Renewal را تست کنید. HSTS را فقط پس از اطمینان از HTTPS کامل و اثر آن روی دامنه/زیردامنه‌ها فعال کنید.

## استقرار Frontend
برای سایت Static/SPA معمولاً Build تولید می‌شود و Artifact در Web Root یا Object/CDN قرار می‌گیرد. SPA نیاز دارد Routeهای سمت Client در Web Server درست fallback شوند. Cache فایل‌های hash شده می‌تواند طولانی و HTML کوتاه‌تر باشد.

## استقرار Backend
Backend را با کاربر غیر root اجرا کنید. Environment Variableها را خارج از Repository نگه دارید. Process باید قابل Restart، Health Check و Log باشد. Nginx می‌تواند درخواست را به Backend Proxy کند.

## Database Migration
Migration باید نسخه‌بندی و قبل از اجرا Backup/Compatibility آن بررسی شود. تغییر Schema ناسازگار می‌تواند Rollback کد را غیرممکن کند؛ در سیستم حساس از Migrationهای backward-compatible استفاده کنید.

## Cloudflare و CDN
DNS دامنه را مدیریت کنید، Proxy را آگاهانه فعال کنید و تفاوت Cache در Edge و Origin را بدانید. CDN فایل را نزدیک‌تر به کاربر تحویل می‌دهد اما Cache Key و Purge اشتباه می‌تواند نسخه قدیمی یا داده نامناسب نمایش دهد. برای محتوای خصوصی از Cache عمومی بدون طراحی صحیح استفاده نکنید.

## Backup
قاعده 3-2-1: سه نسخه داده، روی دو نوع رسانه/مکان و حداقل یک نسخه خارج از محل اصلی. Backup بدون Restore Test قابل اعتماد نیست. فایل‌ها، دیتابیس، تنظیمات حیاتی و Secret recovery plan را پوشش دهید.

## Cron و Maintenance
کارهای زمان‌بندی‌شده مثل Backup، cleanup و گزارش می‌توانند با Cron/Systemd Timer اجرا شوند. خروجی و شکست Job باید قابل مشاهده باشد.

## پروژه مقدماتی
یک VPS آزمایشی را طراحی کنید: کاربر محدود، SSH Key، Firewall، Nginx، HTTPS، Frontend، Backend پشت Reverse Proxy، Backup روزانه و Runbook بازیابی. در محیط واقعی قبل از اجرای فرمان‌های مخرب Snapshot/Backup داشته باشید.
