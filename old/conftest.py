from fileinput import close

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

@pytest.fixture()
def playwright():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture()
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture()
def page(context):
        page = context.new_page()
        yield page
        page.close()

