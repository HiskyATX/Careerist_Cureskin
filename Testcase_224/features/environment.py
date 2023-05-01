from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
#CH


def browser_init(context):
    """
    :param context: Behave context
    """
    #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/geckodriver.exe')
    #service = Service('/Users/Claudia/gitLessons/Careerist_Cureskin/Testcase_224/chromedriver')
    #service = Service('C:\\Users\\Claudia\\gitLessons\\Careerist_Cureskin\\Testcase_224\\geckodriver.exe')
    #context.driver = webdriver.Chrome(service=service)
    # context.browser = webdriver.Safari()
    context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
