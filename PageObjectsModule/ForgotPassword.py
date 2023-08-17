from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ForgotPassword:
    textbox_username_xpath = "//input[@name='username']"
    link_forgot_password_xpath = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    textbox_reset_password_xpath = "//button[@type='submit']"
    reset_password_validation_xpath = "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"

    def __init__(self, driver):
        self.driver = driver

    def set_forgot_password(self):
        self.driver.find_element(By.XPATH, self.link_forgot_password_xpath).click()

    def set_forgot_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_forgot_reset_password(self):
        self.driver.find_element(By.XPATH, self.textbox_reset_password_xpath).click()

    def set_forgot_link_validation(self):
        validation_text = self.driver.find_element(By.XPATH, self.reset_password_validation_xpath)
        print(validation_text)
        # assert validation_text == "Reset Password link sent successfully"
        # if True:
        #     print("A reset password link has been sent to you via email.")
        # else:
        #     print("If the email does not arrive, please contact your OrangeHRM Administrator.")
