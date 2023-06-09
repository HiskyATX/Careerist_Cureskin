from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
def browser_init(context):
    """
    :param context: Behave context
    """
    #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    # service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/geckodriver.exe')
    #service = Service('/Users/Claudia/gitLessons/Careerist_Cureskin/Testcase_191/chromedriver')
    #service = Service('C:\\Users\\Claudia\\gitLessons\\Careerist_Cureskin\\Testcase_191\\geckodriver.exe')
    #context.driver = webdriver.Chrome(service=service)
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Firefox(service=service)
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


    ##HEADLESS_OPTIONS:##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #         service = service
    # )


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