"""Content tests for https://the-internet.herokuapp.com/context_menu."""

import pytest
import requests

URL = "https://the-internet.herokuapp.com/context_menu"


@pytest.fixture(scope="module")
def page():
    """Download the page once and share it with both tests."""
    response = requests.get(URL, timeout=15)
    response.raise_for_status()  # fail clearly if the site itself is down
    return response.text


def test_instructions_text_is_on_page(page):
    """PASSES: this sentence is on the page."""
    assert "Right-click in the box below to see one called 'the-internet'" in page


def test_alibaba_is_on_page(page):
    """FAILS on purpose: 'Alibaba' is not on the page."""
    assert "Alibaba" in page
