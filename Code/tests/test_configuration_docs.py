import re
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DOC = CODE_DIR / "docs" / "configuration.md"
EXAMPLE_ENV = CODE_DIR / "config" / "example.env"


def documented_settings():
    return set(re.findall(r"^\| `([A-Z][A-Z0-9_]+)` \|", CONFIG_DOC.read_text(), re.M))


def example_settings():
    settings = {}
    for line in EXAMPLE_ENV.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            name, _, value = line.partition("=")
            settings[name] = value
    return settings


def test_example_env_has_every_documented_setting():
    assert documented_settings() == set(example_settings())


def test_example_env_has_no_empty_values():
    assert all(example_settings().values())


def test_example_env_contains_no_real_aws_keys():
    text = EXAMPLE_ENV.read_text()
    assert not re.search(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b", text)
    assert "AWS_ACCESS_KEY_ID" not in text
    assert "AWS_SECRET_ACCESS_KEY" not in text
