import time

import pytest
from selenium import webdriver
from PageObjectsModule.MainMenuValidation import MainMenuValidation


class TestCases03:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self, browser_launch):
        self.driver = browser_launch
        self.driver.get(self.base_url)
        time.sleep(5)
        self.mmv = MainMenuValidation(self.driver)
        self.mmv.set_username(self.username)
        self.mmv.set_password(self.password)
        self.mmv.set_login()
        time.sleep(5)
        self.mmv.set_main_menu_validation()
        time.sleep(5)
        self.driver.quit()

