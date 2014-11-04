from selenium import webdriver
import unittest


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_sees_home_page_and_login_link(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Track Expenses', self.browser.title)
        self.browser.find_element_by_id('manage_expense_link_id')
        self.browser.find_element_by_id('login_link_id')

        
    def test_user_click_login_from_home_page_goes_to_home_page_and_is_logged_in(self):
        self.browser.get('http://localhost:8000')
        manage_expense_link = self.browser.find_element_by_id('manage_expense_link_id')
        login_link = self.browser.find_element_by_id('login_link_id')
        
        login_link.click()
        username_field = self.browser.find_element_by_id('id_username')
        password_field = self.browser.find_element_by_id('id_password')
        
        username_field.send_keys("nikhil")
        password_field.send_keys("password")

        login_button = self.browser.find_element_by_id("login_button_id")
        login_button.click()
        self.assertIn('Welcome to Track Expenses', self.browser.title)

    def test_user_clicks_manage_expenses_and_sees_expenses_list(self):
        self.browser.get('http://localhost:8000')
        manage_expense_link = self.browser.find_element_by_id('manage_expense_link_id')
        login_link = self.browser.find_element_by_id('login_link_id')
        manage_expense_link.click()
        username_field = self.browser.find_element_by_id('id_username')
        password_field = self.browser.find_element_by_id('id_password')
        
        username_field.send_keys("nikhil")
        password_field.send_keys("password")

        login_button = self.browser.find_element_by_id("login_button_id")
        login_button.click()
        self.assertIn('Expenses List', self.browser.title)


# This is the simplest way to run this test
# if __name__ == '__main__':
#    unittest.main()

# Below is the alternate way to run this test
# Refer https://docs.python.org/2/library/unittest.html

suite = unittest.TestLoader().loadTestsFromTestCase(NewUserTest)
unittest.TextTestRunner(verbosity=2).run(suite)
