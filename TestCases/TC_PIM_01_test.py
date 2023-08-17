import time

from PageObjectsModule.ForgotPassword import ForgotPassword


class TestCases01:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"

    def test_login(self, browser_launch):
        self.driver = browser_launch
        self.driver.get(self.base_url)
        time.sleep(5)
        self.fgp = ForgotPassword(self.driver)
        self.fgp.set_forgot_password()
        time.sleep(5)
        self.fgp.set_forgot_username(self.username)
        time.sleep(5)
        self.fgp.set_forgot_reset_password()
        time.sleep(5)
        self.fgp.set_forgot_link_validation()
        time.sleep(5)
        self.driver.quit()
