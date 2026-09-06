#!/usr/bin/env python3
"""Repository-wide integrity validator for AS Academy MainCourse.

This validator intentionally stays content-only: it understands the Foundation
contract and filesystem integrity, but owns no Android/runtime behavior.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "courses"
CONTRACT = ROOT / "integration" / "contract.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
LOCAL_FILE_KEYS = {
    "relativepath",
    "filepath",
    "assetpath",
    "sourcefile",
    "resourcefile",
    "localfile",
}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, path, f"invalid JSON ({exc})")
        return None


def course_root_for(path: Path) -> Path:
    relative = path.relative_to(COURSES)
    return COURSES / relative.parts[0]


def validate_local_reference(course_root: Path, source: Path, value: str, errors: list[str]) -> None:
    if not value or value.startswith(("http://", "https://")):
        return
    candidate = (source.parent / value).resolve()
    try:
        candidate.relative_to(course_root.resolve())
    except ValueError:
        fail(errors, source, f"reference escapes course root: {value}")
        return
    if not candidate.exists():
        fail(errors, source, f"missing referenced file: {value}")


def walk_references(value, course_root: Path, source: Path, errors: list[str], key: str = "") -> None:
    if isinstance(value, dict):
        for child_key, child in value.items():
            walk_references(child, course_root, source, errors, child_key)
    elif isinstance(value, list):
        for child in value:
            walk_references(child, course_root, source, errors, key)
    elif isinstance(value, str):
        lower_key = key.lower()
        if lower_key in {"sha256", "checksum", "packagesha256"} and value and not SHA256.fullmatch(value):
            fail(errors, source, f"{key} must be a 64-character SHA-256 hex digest")
        if lower_key.endswith(("url", "uri")) and value.startswith(("http://", "https://")):
            parsed = urlparse(value)
            if not parsed.netloc:
                fail(errors, source, f"invalid URL in {key}: {value}")
        if lower_key in LOCAL_FILE_KEYS:
            validate_local_reference(course_root, source, value, errors)


def main() -> int:
    errors: list[str] = []
    contract = load_json(CONTRACT, errors)
    if not isinstance(contract, dict):
        print("\n".join(errors), file=sys.stderr)
        return 1

    required = contract.get("courseManifestRequiredFields", [])
    expected_schema = contract.get("contentSchemaVersion")
    manifests = sorted(COURSES.glob("*/course/manifest.json"))
    if not manifests:
        errors.append("courses: no course manifests found")

    seen_course_ids: dict[str, Path] = {}
    canonical = 0

    parsed_cache: dict[Path, object] = {}
    for path in sorted(COURSES.rglob("*.json")):
        parsed_cache[path] = load_json(path, errors)

    for manifest_path in manifests:
        manifest = parsed_cache.get(manifest_path)
        if not isinstance(manifest, dict):
            continue
        course_root = course_root_for(manifest_path)
        missing = [field for field in required if field not in manifest]
        if missing:
            fail(errors, manifest_path, f"legacy/non-canonical manifest; missing {missing}")
            continue
        canonical += 1

        course_id = manifest.get("courseId")
        if not isinstance(course_id, str) or not course_id.strip():
            fail(errors, manifest_path, "courseId must be a non-empty string")
        elif course_id in seen_course_ids:
            fail(errors, manifest_path, f"duplicate courseId {course_id!r}; first used by {seen_course_ids[course_id].relative_to(ROOT)}")
        else:
            seen_course_ids[course_id] = manifest_path

        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            fail(errors, manifest_path, f"version must be semantic x.y.z (got {version!r})")

        minimum_core = manifest.get("minimumCoreVersion")
        if not isinstance(minimum_core, str) or not SEMVER.fullmatch(minimum_core):
            fail(errors, manifest_path, f"minimumCoreVersion must be semantic x.y.z (got {minimum_core!r})")

        if manifest.get("contentSchemaVersion") != expected_schema:
            fail(errors, manifest_path, f"contentSchemaVersion {manifest.get('contentSchemaVersion')!r} != Foundation schema {expected_schema!r}")

        walk_references(manifest, course_root, manifest_path, errors)

    for path, payload in parsed_cache.items():
        if payload is not None:
            walk_references(payload, course_root_for(path), path, errors)

    if errors:
        print(f"MainCourse integrity validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(parsed_cache)} JSON files across {canonical} canonical course manifests (schema {expected_schema}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
