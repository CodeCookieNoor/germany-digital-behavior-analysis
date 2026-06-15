from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
SOCIAL_FILE = PROCESSED_DIR / "germany_social_clean.csv"
ECOMMERCE_FILE = PROCESSED_DIR / "germany_ecommerce_clean.csv"
OUTPUT_FILE = PROCESSED_DIR / "germany_demographics_dashboard.csv"


SOCIAL_ACTIVITY_NAMES = {
    "Email Usage": "Email Usage",
    "Online News Reading": "News Reading",
    "Product Information Search": "Info Search",
    "Social Media Participation": "Social Media",
}

AGE_LABELS = {
    "16–24": "16-24",
    "25–64": "25-54",
    "25–54": "25-54",
    "65–74": "55-74",
    "55–74": "55-74",
}

OUTPUT_COLUMNS = [
    "year",
    "source",
    "activity",
    "activity_detail",
    "segment_type",
    "segment",
    "value",
    "demo_type",
    "indicator_name_original",
]


def clean_text(value: str | None) -> str:
    return (value or "").strip()


def normalize_age(value: str) -> str:
    return AGE_LABELS.get(value, value.replace("–", "-"))


def segment_from_row(row: dict[str, str]) -> tuple[str, str]:
    age_group = clean_text(row.get("age_group"))
    education_level = clean_text(row.get("education_level"))
    gender = clean_text(row.get("gender"))

    if education_level:
        return "Education Level", education_level
    if age_group:
        return "Age Group", normalize_age(age_group)
    if gender:
        return "Gender", gender
    return "Overall", "All Individuals"


def read_social_rows() -> list[dict[str, str]]:
    output_rows: list[dict[str, str]] = []

    with SOCIAL_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            original_indicator = clean_text(row.get("indicator_name"))
            activity = SOCIAL_ACTIVITY_NAMES.get(original_indicator)
            if not activity:
                continue

            segment_type, segment = segment_from_row(row)
            value = clean_text(row.get("value"))
            if not value:
                continue

            output_rows.append(
                {
                    "year": clean_text(row.get("year")),
                    "source": "Social",
                    "activity": activity,
                    "activity_detail": original_indicator,
                    "segment_type": segment_type,
                    "segment": segment,
                    "value": value,
                    "demo_type": clean_text(row.get("demo_type")),
                    "indicator_name_original": original_indicator,
                }
            )

    return output_rows


def read_ecommerce_rows() -> list[dict[str, str]]:
    grouped_values: dict[tuple[str, str, str], float] = defaultdict(float)
    grouped_details: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    grouped_demo_type: dict[tuple[str, str, str], str] = {}

    with ECOMMERCE_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = clean_text(row.get("value"))
            if not value:
                continue

            segment_type, segment = segment_from_row(row)
            key = (clean_text(row.get("year")), segment_type, segment)
            grouped_values[key] += float(value)

            original_indicator = clean_text(row.get("indicator_name"))
            if original_indicator not in grouped_details[key]:
                grouped_details[key].append(original_indicator)

            grouped_demo_type[key] = clean_text(row.get("demo_type"))

    output_rows: list[dict[str, str]] = []
    for (year, segment_type, segment), value in sorted(grouped_values.items()):
        output_rows.append(
            {
                "year": year,
                "source": "Ecommerce",
                "activity": "Ecommerce",
                "activity_detail": "All purchase frequency categories",
                "segment_type": segment_type,
                "segment": segment,
                "value": f"{value:.2f}",
                "demo_type": grouped_demo_type.get((year, segment_type, segment), ""),
                "indicator_name_original": " + ".join(grouped_details[(year, segment_type, segment)]),
            }
        )

    return output_rows


def main() -> None:
    rows = read_social_rows() + read_ecommerce_rows()

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
