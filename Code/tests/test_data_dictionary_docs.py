import re
from pathlib import Path

DOC = Path(__file__).resolve().parents[1] / "docs" / "data-dictionary.md"
ENTITIES = ["Company", "Filing", "Financial metric", "Disclosure", "Finding", "Risk score"]
COLUMNS = ["Field", "Meaning", "Type", "Unit", "Period", "Source reference", "Empty"]
INFORMATION_TYPES = {"extracted fact", "detected anomaly", "AI interpretation"}


def entity_table(entity):
    section = DOC.read_text().split(f"\n## {entity}\n", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("|")]
    header = [cell.strip() for cell in rows[0].strip("|").split("|")]
    body = [[cell.strip() for cell in row.strip("|").split("|")] for row in rows[2:]]
    return header, body


def test_every_entity_has_a_table_with_the_required_columns():
    for entity in ENTITIES:
        header, body = entity_table(entity)
        assert header[: len(COLUMNS)] == COLUMNS, entity
        assert body, entity
        for row in body:
            assert len(row) == len(header) and all(row), (entity, row)


def test_every_finding_field_has_an_information_type():
    header, body = entity_table("Finding")
    column = header.index("Information type")
    assert {row[column] for row in body} <= INFORMATION_TYPES


def test_empty_column_says_yes_or_no():
    for entity in ENTITIES:
        header, body = entity_table(entity)
        column = header.index("Empty")
        for row in body:
            assert re.match(r"^(yes|no)\b", row[column]), (entity, row)
