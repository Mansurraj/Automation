# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_createAccount(self):
        self.driver.get("https://brsupplies-hana-test.azurewebsites.net/Login/Index")
        self.driver.set_window_size(1366, 738)
        self.driver.find_element(By.LINK_TEXT, "Create an Account").click()
        self.driver.find_element(By.ID, "FirstName").click()
        self.driver.find_element(By.ID, "FirstName").send_keys("TEST")
        self.driver.find_element(By.ID, "LastName").send_keys("USER")
        self.driver.find_element(By.ID, "EmailAddress").send_keys("mansurraj.891+198@gmail.com")
        self.driver.find_element(By.ID, "Password").click()
        self.driver.find_element(By.ID, "Password").send_keys("Qwerty123@")
        self.driver.find_element(By.ID, "CommunucationOptIn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.ID, "AcceptEula").click()
        self.driver.find_element(By.CSS_SELECTOR, ".acceptEulaButton").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

