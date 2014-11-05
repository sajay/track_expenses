from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

    def test_login_and_add_expense(self):
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
        
        add_expense_link =self.browser.find_element_by_id("add_expense_link_id")
        add_expense_link.click()
        self.assertIn('Add Expenses', self.browser.title)
        

        expense_category_select = Select(self.browser.find_element_by_id('id_expenseCategory'))

        selected_category = expense_category_select.options[3].text
        expense_category_select.select_by_visible_text(selected_category)

        #print [o.text for o in expense_category_select.options]
        

        expense_type_select = Select(self.browser.find_element_by_id('id_expenseType'))
        expense_type_select.select_by_visible_text(expense_type_select.options[0].text)

        
        vendor_type_select = Select(self.browser.find_element_by_id('id_vendorType'))
        vendor_type_select.select_by_visible_text(vendor_type_select.options[0].text)
        
        expense_date_field = self.browser.find_element_by_id("id_expense_date")
        expense_date_field.send_keys("Apr 01, 2014")

        amount_spent_field = self.browser.find_element_by_id("id_amount_spent")
        amount_spent_field.send_keys("10")

        comments_field = self.browser.find_element_by_id("id_comments")
        comments_field.send_keys("This is a comment for the Functional Test expense.") 
        self.browser.implicitly_wait(6)

        add_button = self.browser.find_element_by_id("add_button_id")
        add_button.click()
        self.assertIn('Expenses List', self.browser.title)





# This is the simplest way to run this test
# if __name__ == '__main__':
#    unittest.main()

# Below is the alternate way to run this test
# Refer https://docs.python.org/2/library/unittest.html

suite = unittest.TestLoader().loadTestsFromTestCase(NewUserTest)
unittest.TextTestRunner(verbosity=2).run(suite)
