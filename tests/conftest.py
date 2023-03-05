import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.hold_browser_open = True
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
