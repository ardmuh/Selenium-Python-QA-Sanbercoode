import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.saucedemo.com/"

class TugasDay17(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_succesfuly_login_with_valid_username_and_password(self):
        self.driver.get(url)
        time.sleep(1)
        user_name = self.driver.find_element(By.ID, 'user-name')
        user_name.send_keys("standard_user")
        time.sleep(0.5)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        response = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        self.assertEqual(response, 'PRODUCTS')

    def test_failed_login_with_empty_username_and_password(self):
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username is required')

    def test_failed_login_with_invalid_username_or_password(self):
        self.driver.get(url)
        time.sleep(1)
        user_name = self.driver.find_element(By.ID, 'user-name')
        user_name.send_keys("standard_user")
        time.sleep(0.5)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("invalid-pass")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username and password do not match any user in this service')

    def test_failed_login_with_empty_username(self):
        self.driver.get(url)
        time.sleep(1)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username is required')
    
    def test_failed_login_with_empty_password(self):
        self.driver.get(url)
        time.sleep(1)
        user_name = self.driver.find_element(By.ID, 'user-name')
        user_name.send_keys("standard_user")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Password is required')

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()