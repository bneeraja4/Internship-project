from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SigninPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from pages.add_project_page import AddProjectPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)
        self.product_page = ProductPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)
        self.add_project_page = AddProjectPage(driver)