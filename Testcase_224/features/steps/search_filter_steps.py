from behave import when, then, given
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

@given('Open Cureskin page')
def open_cureskin_page(self):
    self.app.main_page.open_main_url()


@when('Clicking on Shop All section')
def click_shop_all(self):
    self.app.main_page.wait_for_element_appear(*self.app.main_page.SHOP_ALL)
#    self.app.main_page.wait_for_shop_all_to_appear()
    self.app.main_page.click(*self.app.main_page.SHOP_ALL)


@when('Adjusting the Price Filter')
def adjust_price_filter(self):
    right_slider = self.driver.find_element (By.XPATH, "//*[@id='FacetDrawer']/div/div/details[2]/div/price-range/div[2]/div[4]")
    left_slider = self.driver.find_element (By.XPATH,  "//*[@id='FacetDrawer']/div/div/details[2]/div/price-range/div[2]/div[3]")
    ActionChains(self.driver).drag_and_drop_by_offset(left_slider, 80, 0).perform()
    ActionChains(self.driver).drag_and_drop_by_offset(right_slider, -80, 0).perform()
    sleep(2)


@then('Verify that products displayed are within the Price filter')
def products_displayed_corresponds_filter(self):
    min, max = self.app.main_page.find_range()
    self.app.main_page.compare_product_prices()
    pass

