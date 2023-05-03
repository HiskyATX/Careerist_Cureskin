import allure
from allure_commons.types import AttachmentType
from app.application import Application
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from support.logger import logger, MyListener

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver.exe')
    service = Service('/Users/svetlanalevinsohn/JobEasy/12-python-selenium-automation/geckodriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # # for browerstack ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)

def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
#
#_______________________________________________________________________________________________________________________
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from app.application import Application
# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#     #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver.exe')
#     service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/geckodriver.exe')
#     #service = Service('/Users/Claudia/Documents/Mom/CAREERIST/Automation/Lesson07/chromedriver.exe')
#     #context.driver = webdriver.Chrome(service=service)
#     # context.driver = webdriver.Safari()
#     context.driver = webdriver.Firefox(service=service)
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, 10)
#     context.app = Application(driver=context.driver)
#
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, feature):
#     context.driver.quit()

#_______________________________________________________________________________________________________________________
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from app.application import Application
# def browser_init(context):
# # def browser_init(context, test_name):
#     """
#     :param context: Behave context
#     """
#     #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
#     service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/geckodriver.exe')
#     #service = Service('/Users/Claudia/gitLessons/Careerist_Cureskin/Testcase_224/chromedriver')
#     #service = Service('C:\\Users\\Claudia\\gitLessons\\Careerist_Cureskin\\Testcase_224\\geckodriver.exe')
#     #context.driver = webdriver.Chrome(service=service)
#     #context.browser = webdriver.Safari()
#     context.driver = webdriver.Firefox(service=service)
#
#
#     ###### for browserstack ########
#     # desired_cap = {
#     #     'browserName': 'Firefox',
#     #     'bstack:options': {
#     #         'os': 'Windows',
#     #         'osVersion': '10',
#     #         'sessionName': test_name
#     #     }
#     # }
#     #
#     # bs_user = 'claudiahisky_IML8gh'
#     # bs_key = 'hAKJnzV9zmgPnYWxcveP'
#     # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
#
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, 10)
#     context.app = Application(driver=context.driver)
#
#
#     ##HEADLESS_OPTIONS:##
#     # options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     # context.driver = webdriver.Chrome(
#     #     chrome_options=options,
#     #         service = service
#     # )
#
#
# # def before_scenario(context):
# #     print('\nStarted scenario: ', scenario.name)
# #     #browser_init(context, scenario.name)
# #     browser_init(context)
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     #browser_init(context, scenario.name)
#     #browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, feature):
#     context.driver.quit()
