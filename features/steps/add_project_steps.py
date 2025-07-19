from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open the main page')
def open_main(context):
    context.app.login_page.open_main()

@when('Log in to the page')
def login(context):
    context.app.login_page.login("bneeraja4@gmail.com", "Aparna@704")

@when('Click on the settings option')
def click_settings(context):
    context.app.settings_page.click_settings()

@when('Click on Add a project')
def click_add_project(context):
    context.app.settings_page.click_add_project()

@then('Verify the Add Project page is displayed')
def verify_add_project_page(context):
    assert context.app.add_project_page.is_loaded()

@when('Add some test information to the input fields')
def fill_form(context):
    context.app.add_project_page.fill_form(name="kim",company="abcd",role="Developer",country="USA",phone="123456")

@then('Verify the right information is present in the input fields')
def verify_form_values(context):
    context.app.add_project_page.verify_form_values(name="kim",company="abcd",role="Developer",country="USA",phone="123456")

@then('Verify the “Send an application” button is available and clickable')
def verify_button(context):
    assert context.app.add_project_page.is_send_button_clickable()
