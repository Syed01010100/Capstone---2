from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from Locators.LOCATORS import AdminPageLocators


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_admin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AdminPageLocators.ADMIN_TAB)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/web/index.php/admin/viewSystemUsers")
        )


    def is_element_visible(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element.text
        except Exception as e:
            print(f"Error finding element at '{xpath}': {e}")
            return None

    def validate_visible_options(self, expected_options):
        visible_options = []
        for option in expected_options:
            option_xpath = f"//span[text()='{option}'] | //a[span[text()='{option}']]"
            if self.is_element_visible(option_xpath):
                visible_options.append(option)
        return visible_options