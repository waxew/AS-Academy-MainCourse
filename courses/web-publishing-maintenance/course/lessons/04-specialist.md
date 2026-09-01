# سطح تخصصی — Production Engineering و SRE

## High Availability
هدف HA کاهش Single Point of Failure است. چند instance پشت Load Balancer، Health Check، دیتابیس مقاوم و Edge صحیح اجزای رایج‌اند. Stateless کردن Application Tier، Scale افقی را ساده‌تر می‌کند.

## Load Balancing
الگوریتم‌هایی مثل round-robin و least-connections وجود دارند. Health Check باید instance ناسالم را از ترافیک خارج کند. Sticky Session وابستگی ایجاد می‌کند و باید آگاهانه استفاده شود.

## Zero-Downtime Deployment
Blue/Green دو محیط مشابه دارد و ترافیک بین آن‌ها جابه‌جا می‌شود. Canary نسخه جدید را ابتدا به درصد کمی می‌دهد. Rolling Update instanceها را تدریجی تعویض می‌کند. سازگاری دیتابیس و Observability شرط حیاتی‌اند.

## Feature Flag و Release Engineering
Feature Flag قابلیت را از Deploy جدا می‌کند و باید Owner/تاریخ حذف داشته باشد. Artifact immutable، نسخه قابل ردیابی، Changelog، Migration Plan، Approval، Verification و Rollback پایه Release سالم‌اند. Commit SHA، Image digest و Release version باید قابل ارتباط باشند.

## Supply Chain Security
Dependency، Registry، CI Runner، Action ثالث و Artifact بخشی از زنجیره تأمین‌اند. نسخه‌ها را Pin، Permissionها را محدود و Dependency/Artifact را Scan و قابل ردیابی کنید.

## Security Header و Threat Modeling
CSP، HSTS، X-Content-Type-Options و سیاست‌های Referrer/Permissions بر اساس نیاز تنظیم می‌شوند. CSP بهتر است ابتدا report-only ارزیابی شود. در Threat Modeling، Asset، Trust Boundary، Entry Point، Actor، Threat و Detection را مشخص کنید.

## Observability
Logs، Metrics و Traces سه سیگنال مهم‌اند. Correlation ID مسیر درخواست را میان سرویس‌ها دنبال می‌کند. Dashboard باید سؤال عملیاتی مشخص پاسخ دهد.

## SLI، SLO و SLA
SLI اندازه‌گیری مانند availability/latency، SLO هدف داخلی کیفیت و SLA تعهد قراردادی است. Error Budget تعادل Reliability و سرعت تغییر را پشتیبانی می‌کند.

## Incident و Postmortem
چرخه Incident: Detect → Triage → Mitigate → Communicate → Recover → Learn. ابتدا سرویس را پایدار و سپس Root Cause را بررسی کنید. Postmortem روی علت‌های سیستمی، Detection gap و Action Item قابل پیگیری تمرکز می‌کند.

## Disaster Recovery
RPO حداکثر داده قابل از دست رفتن و RTO حداکثر زمان بازیابی قابل قبول است. Backup Strategy باید از آن‌ها مشتق شود. Restore Drill دوره‌ای ضروری است.

## Database Production
Connection Pool، Slow Query، Index، Lock، Migration، Replication و Backup را پایش کنید. Migration پرریسک را به expand/migrate/contract تقسیم کنید تا سازگاری Release حفظ شود.

## Capacity و Cost
CPU، RAM، Disk IOPS، Network، Connection، Peak و نرخ رشد را اندازه‌گیری کنید. Capacity Planning باید داده‌محور باشد.

## نگهداری بلندمدت
تقویم Patch، Dependency Update، Certificate/Domain Renewal، Restore Test، Security Review، Performance Audit، SEO Audit و حذف Feature Flagهای قدیمی بسازید.

## Capstone تخصصی
سامانه‌ای شامل Frontend، API و Database را برای Production طراحی کنید. تحویل: Architecture Diagram، DNS، TLS، Docker/Runtime، CI/CD، Secret Management، WAF/Rate Limit، OWASP Checklist، Monitoring/Alert، Backup با RPO/RTO، Runbook، Rollback، Core Web Vitals، Technical SEO، Analytics Plan، Privacy Plan و Incident Scenario.

معیار قبولی: توانایی مدیریت Deploy خراب، انقضای Certificate، Disk Full، افزایش 5xx، Migration ناموفق، از دست رفتن Node و Restore دیتابیس با Runbook.
