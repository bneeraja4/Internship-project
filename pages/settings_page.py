from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class SettingsPage(Page):
    SETTINGS_BTN = (By.XPATH, "//*[text()='Settings']")
    ADD_PROJECT_BTN = (By.XPATH, "//*[text()='Add a project']")

    def click_settings(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SETTINGS_BTN)).click()

    def click_add_project(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_PROJECT_BTN)).click()
