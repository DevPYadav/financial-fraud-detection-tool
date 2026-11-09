from pathlib import Path

DOC = Path(__file__).resolve().parents[1] / "docs" / "company-selection-criteria.md"
SECTORS = [
    "Banking",
    "Financial services",
    "Information technology",
    "Pharmaceuticals",
    "Manufacturing",
    "Retail",
    "Infrastructure",
]


def test_sample_is_seven_red_flag_and_three_control():
    text = DOC.read_text()
    assert "**7 red-flag companies:**" in text
    assert "**3 control companies:**" in text


def test_all_scope_sectors_are_listed():
    text = DOC.read_text()
    for sector in SECTORS:
        assert f". {sector}\n" in text, sector


def test_required_sections_exist():
    text = DOC.read_text()
    for heading in [
        "## What qualifies as a red-flag company",
        "## What qualifies as \"no known allegations\" (control)",
        "## Data availability",
        "## Delisted, merged or renamed companies",
        "## Client approval",
    ]:
        assert heading in text, heading
