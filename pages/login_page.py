from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
     EMAIL = (By.ID, 'email-2')
     PASSWORD = (By.ID, 'field')
     CONTINUE_BTN = (By.XPATH, "//*[text()='Continue']")

     def open_main(self):
         self.driver.get('https://soft.reelly.io/sign-in')

     def login(self, email, password):
         self.input_text(self.EMAIL, email)
         self.input_text(self.PASSWORD, password)
         self.click(*self.CONTINUE_BTN)


