from selenium import webdriver
import unittest


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_sees_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Track Expenses', self.browser.title)

if __name__ == '__main__':
    unittest.main()
