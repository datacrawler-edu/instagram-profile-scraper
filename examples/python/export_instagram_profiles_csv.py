"""Export saved Instagram profile Dataset JSON to a useful CSV view."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "success",
    "status",
    "input",
    "username",
    "profileUrl",
    "duplicateOf",
    "scrapedAt",
    "attempts",
    "responseTimeMs",
    "fullName",
    "biography",
    "followersCount",
    "followsCount",
    "postsCount",
    "isVerified",
    "isPrivate",
    "accountTypeName",
    "category",
    "externalUrl",
    "bioLinks",
    "profilePicUrl",
    "profilePicUrlHD",
    "pronouns",
    "location",
    "dataQuality",
    "error",
]


def json_value(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return value


def row_from_item(item: dict[str, Any]) -> dict[str, Any]:
    profile = item.get("profile") or {}
    return {
        "success": item.get("success"),
        "status": item.get("status"),
        "input": item.get("input"),
        "username": item.get("username"),
        "profileUrl": item.get("profileUrl"),
        "duplicateOf": item.get("duplicateOf"),
        "scrapedAt": item.get("scrapedAt"),
        "attempts": item.get("attempts"),
        "responseTimeMs": item.get("responseTimeMs"),
        "fullName": profile.get("fullName"),
        "biography": profile.get("biography"),
        "followersCount": profile.get("followersCount"),
        "followsCount": profile.get("followsCount"),
        "postsCount": profile.get("postsCount"),
        "isVerified": profile.get("isVerified"),
        "isPrivate": profile.get("isPrivate"),
        "accountTypeName": profile.get("accountTypeName"),
        "category": profile.get("category"),
        "externalUrl": profile.get("externalUrl"),
        "bioLinks": json_value(profile.get("bioLinks")),
        "profilePicUrl": profile.get("profilePicUrl"),
        "profilePicUrlHD": profile.get("profilePicUrlHD"),
        "pronouns": json_value(profile.get("pronouns")),
        "location": json_value(profile.get("location")),
        "dataQuality": json_value(profile.get("dataQuality")),
        "error": json_value(item.get("error")),
    }


def export_csv(input_path: Path, output_path: Path) -> None:
    items = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise ValueError("The input JSON must contain a list of Dataset items.")

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_from_item(item) for item in items)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", type=Path, nargs="?", default=Path("data/sample-output.json")
    )
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        default=Path("data/exported-instagram-profiles.csv"),
    )
    args = parser.parse_args()
    export_csv(args.input, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
