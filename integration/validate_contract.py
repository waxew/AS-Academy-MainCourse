#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "integration" / "contract.json").read_text(encoding="utf-8"))
required = set(contract["courseManifestRequiredFields"])
schema = contract["contentSchemaVersion"]
core_version = tuple(map(int, contract["coreVersion"].split(".")))
semver = re.compile(r"^\d+\.\d+\.\d+$")
errors = []
seen_ids = set()
manifests = sorted((ROOT / "courses").glob("*/course/manifest.json"))

if not manifests:
    errors.append("No course manifests found")

for path in manifests:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        continue

    missing = sorted(required - data.keys())
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")

    course_id = data.get("courseId")
    if not isinstance(course_id, str) or not course_id.strip():
        errors.append(f"{path}: courseId must be a non-empty string")
    elif course_id in seen_ids:
        errors.append(f"{path}: duplicate courseId {course_id}")
    else:
        seen_ids.add(course_id)

    if data.get("contentSchemaVersion") != schema:
        errors.append(f"{path}: contentSchemaVersion must be {schema}")

    version = data.get("version")
    minimum = data.get("minimumCoreVersion")
    if not isinstance(version, str) or not semver.match(version):
        errors.append(f"{path}: version must use x.y.z semantic versioning")
    if not isinstance(minimum, str) or not semver.match(minimum):
        errors.append(f"{path}: minimumCoreVersion must use x.y.z semantic versioning")
    else:
        min_tuple = tuple(map(int, minimum.split(".")))
        if min_tuple > core_version:
            errors.append(f"{path}: requires Core {minimum}, newer than foundation Core {contract['coreVersion']}")

if errors:
    print("Foundation course validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(f"Foundation contract OK: validated {len(manifests)} course manifests against schema {schema}")
