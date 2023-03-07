import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.hold_browser_open = True
    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
