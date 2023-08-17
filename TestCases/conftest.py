from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def browser_launch():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
