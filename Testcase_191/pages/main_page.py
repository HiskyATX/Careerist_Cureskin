from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    PRODUCT_COUNT = (By.XPATH, "//*[@id='ProductCount']")

    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')


    def search_for_cure(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')
        self.wait_for_element_appear(*self.PRODUCT_COUNT)


    def find_element_text(self):
        actual_search = self.driver.find_element(*self.PRODUCT_COUNT).text
        return actual_search #returning actual_search (string) to be passed later on