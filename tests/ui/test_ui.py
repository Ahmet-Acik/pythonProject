import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options()
    options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'  # Specify the path to the Chrome binary
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get('https://www.google.com')
    assert 'Google' in browser.title