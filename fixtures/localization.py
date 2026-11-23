import json
from pathlib import Path
import pytest
from pages.registration_page import RegistrationFields

LOCALES_DIR = Path(__file__).parent.parent / "locales"


def pytest_addoption(parser):
    parser.addoption(
        "--locales",
        action="store",
        default="en,de",
        help="Comma-separated list of locales (e.g., --locales=en,de)",
    )

def get_locales(config):
    locales_str = config.getoption("--locales")
    return [loc.strip() for loc in locales_str.split(",")]

def pytest_generate_tests(metafunc):
    req_data = ("locale", "field", "reg_empty_error_message")
    if set(req_data).issubset(metafunc.fixturenames):
        locales = get_locales(metafunc.config)
        metafunc.parametrize(req_data, _build_mandatory_fields_messages(locales))


def _load_registration_locales(locale: str):
    path = LOCALES_DIR / locale / "registration.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _build_mandatory_fields_messages(locales: list[str]) -> list:
    params = []
    for locale in locales:
        data = _load_registration_locales(locale)
        for field in RegistrationFields:
            error_msg = data["fields"][field.name]["error_messages"]["missing_field"]
            params.append(pytest.param(locale, field, error_msg, id=f"{locale}-{field.name}"))
    return params
