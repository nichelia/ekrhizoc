import json
from pathlib import Path

import pytest


@pytest.fixture()
def url_data():
    filepath = Path(__file__).parent / "fixtures" / "url_data.json"
    if filepath:
        with open(filepath) as f:
            return json.load(f)
    else:
        return {}


@pytest.fixture()
def canonical_urls():
    filepath = Path(__file__).parent / "fixtures" / "canonical_urls.json"
    if filepath:
        with open(filepath) as f:
            return json.load(f)
    else:
        return {}


@pytest.fixture()
def valid_urls():
    filepath = Path(__file__).parent / "fixtures" / "valid_urls.json"
    if filepath:
        with open(filepath) as f:
            return json.load(f)
    else:
        return []


@pytest.fixture()
def invalid_urls():
    filepath = Path(__file__).parent / "fixtures" / "invalid_urls.json"
    if filepath:
        with open(filepath) as f:
            return json.load(f)
    else:
        return []
