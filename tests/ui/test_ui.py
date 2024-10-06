import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

@pytest.fixture
def browser():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options()

    chrome_path_local = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    chrome_path_ci = '/usr/bin/google-chrome'

    if os.path.exists(chrome_path_local):
        options.binary_location = chrome_path_local
    else:
        options.binary_location = chrome_path_ci

    if os.getenv('CI'):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get('https://www.google.com')
    assert 'Google' in browser.title

def test_google_search_fail(browser):
    browser.get('https://www.google.com')
    assert 'Yahoo' not in browser.title

def test_wikipedia_search(browser):
    browser.get('https://www.wikipedia.org')

    search_box = browser.find_element('name', 'search')
    search_box.send_keys('Python (programming language)')
    time.sleep(2)
    search_box.submit()
    time.sleep(2)
    assert 'Python (programming language) - Wikipedia' in browser.title