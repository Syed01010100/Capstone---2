# Import necessary libraries
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.forgot_password_page import ForgotPasswordPage
from Pages.admin_page import AdminPage
from Excel_Function.excel_functions import ExcelFunctions

# Test class for OrangeHRM
class TestOrangeHRM:
    """Test suite for testing functionality in OrangeHRM."""

    # Fixture for browser session setup and teardown
    @pytest.fixture(autouse=True)
    def setup_browser_session(self):
        """Setup the browser session and generate page object instances."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Initialize page objects
        self.login_page = LoginPage(self.driver)
        self.forgot_password_page = ForgotPasswordPage(self.driver)
        self.admin_page = AdminPage(self.driver)
        self.excel = ExcelFunctions("C:\\Users\\Nadeem\\Desktop\\Capstone - 2\\Data\\OrangeHRM_Test_Scenario.xlsx", "Sheet1")

        yield  # Execute tests

        # Cleanup: Close the browser after tests
        self.driver.quit()

    def test_forget_password_link(self):
        """Test the password reset functionality with a valid username."""
        # Click the 'Forgot Password' link and reset password
        self.login_page.click_forgot_password()
        self.forgot_password_page.enter_username("Admin")
        self.forgot_password_page.click_reset()

        # Verify the success message
        success_message = self.forgot_password_page.get_success_message()
        assert success_message == "Reset Password link sent successfully"

        # Log the result in Excel
        self.excel.write_data(2, 6, "Pass" if success_message == "Reset Password link sent successfully" else "Fail")

    def test_admin_menu(self):
        """Verify visibility of expected options in the Admin module."""
        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()

        # Expected options in the Admin module
        expected_options = [
            "User Management",
            "Job",
            "Organization",
            "Qualifications",
            "Nationalities",
            "Corporate Branding",
            "Configuration"
        ]

        # Gather actual options from the page
        actual_options = [
            self.admin_page.get_element_text(f"//nav/ul/li[span[contains(text(), '{option}')]] | //nav/ul/li[a[contains(text(), '{option}')]]").strip()
            for option in expected_options
            if self.admin_page.get_element_text(f"//nav/ul/li[span[contains(text(), '{option}')]] | //nav/ul/li[a[contains(text(), '{option}')]]").strip()
        ]

        # Log and assert results
        assert actual_options == expected_options, f"Expected options '{expected_options}' but found '{actual_options}'"
        self.excel.write_data(3, 6, "Pass" if actual_options == expected_options else "Fail")

    def test_side_menu(self):
        """Verify visibility of expected options in the side menu of the Admin module."""
        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()

        # Expected options in the side menu
        expected_side_menu = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Maintenance",
            "Buzz"
        ]

        # Validate visible options
        actual_side_menu = self.admin_page.validate_visible_options(expected_side_menu)

        # Assert the result and log in Excel
        assert sorted(actual_side_menu) == sorted(expected_side_menu), f"Expected options '{expected_side_menu}' but found '{actual_side_menu}'"
        self.excel.write_data(4, 6, "Pass" if sorted(actual_side_menu) == sorted(expected_side_menu) else "Fail")
