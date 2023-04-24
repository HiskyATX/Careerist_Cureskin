from behave import when, then, given


@given ('Open page at Cure keyword')
def open_page_cure_keyword(self):
    self.app.main_page.search_for_cure()


@then('Verify search has {expected_count} item(s)')
def check_number_of_products(self, expected_count):
    actual_search = self.app.main_page.find_element_text()
    number_of_products = actual_search.split()[0]   #splitting the string and handling it as a list. Using
                                                    #first element of the list for element comparison, as it contains
                                                    #the actual number of items in the search

    assert number_of_products == expected_count, f'Expected {expected_count} number of items, but got {number_of_products} item(s).'
