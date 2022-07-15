from base_page import BasePage
from main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def get_title(self):
        return self.driver.title

    def get_header_main_page(self):
        return self.find_element(MainPageLocators.MAIN_PAGE_WELCOME).text

    def open_books_page(self):
        books_link = self.find_element(MainPageLocators.BOOKS_LOCATOR)
        books_link.click()

    def open_fiction_page(self):
        clothing_fiction = self.find_element(MainPageLocators.
                                             FICTION_CLOTHING_LOCATORS)
        clothing_fiction.click()
        fiction_locators = self.find_element(MainPageLocators.FICTION_LOCATORS)
        fiction_locators.click()

    def open_basket(self):
        view_basket = self.find_element(MainPageLocators.VIEW_BASKET)
        view_basket.click()
