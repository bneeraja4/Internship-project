from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class AddProjectPage(Page):
    TITLE = (By.CSS_SELECTOR, "[class='h2-text book']")
    NAME_INPUT = (By.ID, "Your-name")
    COMPANY_NAME_INPUT = (By.ID, "Your-company-name")
    ROLE_INPUT = (By.ID, "Role")
    COUNTRY_INPUT = (By.ID, "Country")
    PHONE_INPUT = (By.ID, "Phone")
    SEND_BTN = (By.CSS_SELECTOR, "[class='purchase-access w-button']")

    def is_loaded(self):
        sleep(5)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TITLE))

    def fill_form(self, name="", company="", role="", country="", phone=""):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.COMPANY_NAME_INPUT, company)
        self.input_text(self.ROLE_INPUT, role)
        self.input_text(self.COUNTRY_INPUT, country)
        self.input_text(self.PHONE_INPUT, phone)

    def verify_form_values(self, name, company, role, country, phone):
        assert (self.find_element_value(self.NAME_INPUT).strip() == name and
                self.find_element_value(self.COMPANY_NAME_INPUT).strip() == company and
                self.find_element_value(self.ROLE_INPUT).strip() == role and
                self.find_element_value(self.COUNTRY_INPUT).strip() == country and
                self.find_element_value(self.PHONE_INPUT).strip() == phone)

    def is_send_button_clickable(self):
        return self.is_element_enabled(self.SEND_BTN)

