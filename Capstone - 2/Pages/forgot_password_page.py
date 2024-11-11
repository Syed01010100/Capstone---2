from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators_test import ForgotPasswordPageLocators


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ForgotPasswordPageLocators.USERNAME_FIELD)
        ).send_keys(username)

    def click_reset(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
        ).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ForgotPasswordPageLocators.SUCCESS_MESSAGE)
        ).text