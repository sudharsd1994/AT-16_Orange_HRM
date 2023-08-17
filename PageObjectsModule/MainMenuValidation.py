from selenium.webdriver.common.by import By


class MainMenuValidation:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    main_menu_validation_xpath = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def set_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def set_main_menu_validation(self):
        element = self.driver.find_elements(By.XPATH, self.main_menu_validation_xpath)
        print(len(element))
        for element01 in element:
            print(element01)
            break



