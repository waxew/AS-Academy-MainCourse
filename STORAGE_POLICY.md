# AS Academy Content Storage Policy

MainCourse is the single editable source of educational content. Educational files must never be stored in the application database.

## Canonical locations

- Editable source: `courses/<course-id>/course/` in `AS-Academy-MainCourse`.
- Bundled fallback: compiled Course Package embedded in the host APK at build time.
- Runtime package: immutable/rolling external content asset (currently GitHub Releases for the Basic channel) served over HTTPS.
- Supabase Postgres: only small release metadata and authenticated user-state sync records.
- Device Room database: only user state such as progress, notes, quiz history, bookmarks, drafts, achievements, flashcard review state, and the bounded sync outbox.

## Database exclusions

The following must not be stored in Postgres or Room as durable Course content:

- compiled Course Packages
- lesson bodies or duplicated Search text
- videos, audio, images, PDFs or archives
- large code/data assets

Search indexes are derived from the Course Package loaded in memory. Sync payloads are bounded to 64 KiB by Core and Supabase so they cannot become an accidental file store.

## Release integrity

Every runtime package must be validated and compiled with the immutable Foundation Core compiler, published outside the database, and paired with metadata containing `courseId`, `version`, `contentSchemaVersion`, `minimumCoreVersion`, `sha256`, and an HTTPS `downloadUrl`.
