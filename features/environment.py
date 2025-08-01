from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome()
    #context.browser = webdriver.Safari()
    #context.driver = webdriver.Firefox()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)

    ## BROWSERSTACK ###
    # bs_user ='bneeraja_dc1OHz'
    # bs_key = 'pn8bctDxP7ynceh5icmi'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #      "os" : "Windows",
    #      "osVersion" : "11",
    #      'browserName': 'Chrome',
    #      'sessionName': scenario_name,
    #  }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # ## BROWSERSTACK mobile web###
    # bs_user ='bneeraja_dc1OHz'
    # bs_key = 'pn8bctDxP7ynceh5icmi'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     "deviceName": "Pixel 7",
    #      "os" : "Windows",
    #      "osVersion" : "12",
    #      'browserName': 'Chrome',
    #      'sessionName': scenario_name,
    #  }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ###Mobile emulation Chrome
    mobile_emulation = {"deviceName": "Pixel 7"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #run locally
    context.driver = webdriver.Chrome(options=chrome_options)

    #context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()