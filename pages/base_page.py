from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
    def find_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        #return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text

    def find_element_value(self, locator):
        value = self.find_element(*locator).get_attribute("value")
        print(value)
        return value
    def is_element_enabled(self, locator):
        return self.find_element(*locator).is_enabled()