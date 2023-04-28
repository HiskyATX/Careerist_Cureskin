from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    PRODUCT_COUNT = (By.XPATH, "//*[@id='ProductCount']")
    SHOP_ALL = (By.XPATH, "//span[contains(text(), 'Shop All')]")
    PRICES_RANGE = (By.XPATH, "//div[contains(text(),'Price: Rs.')]")
    # PRODUCT_GRID = (By.XPATH, "//*[@id='product-grid']")
    CARD_INFO = (By.CSS_SELECTOR, ".card-information")
    PRICE_ON_SALE = (By.CSS_SELECTOR, "#product-grid > li:nth-child(1) > div > div > div.card-information__wrapper > div.price.price--on-sale")


    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')
        #self.wait_for_element_appear(*self.SHOP_ALL)


    # def search_for_cure(self):
    #     self.open_url('https://shop.cureskin.com/search?q=cure')
    #     self.wait_for_element_appear(*self.PRODUCT_COUNT)


    def find_element_text(self):
        actual_search = self.driver.find_element(*self.PRODUCT_COUNT).text
        return actual_search #returning actual_search (string) to be passed later on


    def find_range(self):
        find_range = self.driver.find_element(*self.PRICES_RANGE).text
        minimum_price = find_range.split('—')[0]    #splitting the string "Price Rs. 228 — Rs. 429" at the dash & gathering element at index 0
        maximum_price = find_range.split('—')[1]    #the same is done but now gathering element at index 1
        minimum_price = minimum_price.split(' ')[2] #the string "Price Rs. 228" is split at spaces; the element at the 2nd index is gathered
        maximum_price = maximum_price.split(' ')[2] #the string "Rs. 429" is split at spaces; the element at the 1st index is gathered
        maximum_price = float(maximum_price)          #converting to float for comparison use later
        minimum_price = float(minimum_price)

        return minimum_price, maximum_price


    def compare_product_prices(self):
        minimum, maximum = self.find_range()

        all_products = self.driver.find_elements(*self.CARD_INFO)
        price_list_text = [price.text for price in all_products]

        for sale_price in price_list_text:
            sale_price = sale_price.split('Sale price\nRs.')[1]
            sale_price = float(sale_price)

            assert sale_price > minimum and sale_price < maximum, f'Prices are not correct'
        pass


