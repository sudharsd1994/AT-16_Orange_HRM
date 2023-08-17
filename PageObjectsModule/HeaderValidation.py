
from selenium.webdriver.common.by import By


class HeaderValidation:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    admin_link_text = "Admin"
    admin_menu_xpath = "//span[@class='oxd-topbar-body-nav-tab-item']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def set_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def set_admin_click(self):
        self.driver.find_element(By.LINK_TEXT, self.admin_link_text).click()

    def set_admin_menu(self):
        validation_text = self.driver.find_elements(By.XPATH, self.admin_menu_xpath)
        length=len(validation_text)
        print(length)
        for admin in range(length):
            print(admin)








