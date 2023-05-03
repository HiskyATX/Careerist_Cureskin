from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


#def browser_init(context):
def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/geckodriver.exe')
    # #service = Service('/Users/Claudia/gitLessons/Careerist_Cureskin/Testcase_224/chromedriver')
    # #service = Service('C:\\Users\\Claudia\\gitLessons\\Careerist_Cureskin\\Testcase_224\\geckodriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    #context.browser = webdriver.Safari()
    #context.driver = webdriver.Firefox(service=service)

    ###### for browserstack ########
    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_name
        }
    }

    bs_user = 'claudiahisky_IML8gh'
    bs_key = 'hAKJnzV9zmgPnYWxcveP'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)



    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


    ##HEADLESS_OPTIONS:##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #         service = service
    # )





# def before_scenario(context):
#     #print('\nStarted scenario: ', scenario.name)
#     #browser_init(context, scenario.name)
#     browser_init(context)

def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    #browser_init(context, scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
