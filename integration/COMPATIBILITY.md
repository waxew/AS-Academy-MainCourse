# AS Academy Foundation Compatibility Matrix

This file is the human-readable companion to `integration/contract.json`. The JSON contract is authoritative and CI-enforced.

| Foundation baseline | Core | MainUi requires | Content schema | Runtime content schema | minSdk | compileSdk | Java |
|---|---:|---|---:|---:|---:|---:|---:|
| Foundation v1.5 | 1.5.0 | `>=1.5.0 <2.0.0` | 1 | 1 | 23 | 36 | 17 |

## Ownership boundaries

- **AS-Academy-Core** owns runtime composition, persistence, preferences, scheduling, backend adapters, sync/storage infrastructure, content activation and other platform implementation details.
- **AS-Academy-MainUi** owns the shared presentation/design system and consumes only Core public APIs/models.
- **AS-Academy-MainCourse** owns educational content and manifests only; it contains no Android runtime, persistence or backend implementation.
- Future course applications are thin hosts: app identity/configuration + selected course content + Core + MainUi.

## Compatibility policy

- A new public Core API requires a Core minor/major version bump and synchronized contract update across all three repositories.
- A breaking Core API or content-contract change requires a new major contract/baseline.
- Course manifests may retain an older `minimumCoreVersion` when their content does not depend on newer runtime features.
- MainUi must never access Room/DAO/database/backend implementations directly.
- Backend providers such as Supabase must be implemented behind Core-owned abstractions; credentials are never committed.

## Release gate

A Foundation baseline is final only when the three repository contracts are byte-identical, all validators pass, Core unit gates pass, MainUi builds against the checked-out Core, and the `academy-viewer` reference application assembles successfully.
