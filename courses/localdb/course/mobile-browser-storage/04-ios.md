# iOS
Core Data یک object graph و persistence framework است. مفاهیم اصلی: Managed Object Model، Persistent Store، Managed Object Context، Entity، Attribute، Relationship و Fetch Request.

Query با Predicate/Sort انجام می‌شود و import سنگین بهتر است در background context باشد. تغییر مدل نیازمند migration است؛ تغییرات ساده می‌توانند lightweight و تبدیل‌های پیچیده نیازمند migration اختصاصی باشند.

SwiftData مدل Swift-native دارد: @Model، ModelContainer، ModelContext و Query. در پروژه جدید با minimum OS مناسب ساده‌تر است؛ پروژه legacy ممکن است Core Data را نگه دارد یا تدریجی مهاجرت کند.

پروژه: Task Manager با Task/Category relationship، filter/sort و migration افزودن priority همراه تست حفظ داده.
