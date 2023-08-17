import pytest
from selenium import webdriver
import time
from PageObjectsModule.HeaderValidation import HeaderValidation


class TestCases02:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self, browser_launch):
        self.driver = browser_launch
        self.driver.get(self.base_url)
        time.sleep(5)
        self.lp = HeaderValidation(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.set_login()
        time.sleep(5)
        self.lp.set_admin_click()
        time.sleep(5)
        self.lp.set_admin_menu()
        time.sleep(5)
        self.driver.quit()


