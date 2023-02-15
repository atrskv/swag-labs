import pytest
from selene.support.shared import browser

@pytest.fixture()
def browser_management():
    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.hold_browser_open = False