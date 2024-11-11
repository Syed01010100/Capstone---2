from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators_test import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME_FIELD)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

    def click_forgot_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        ).click()