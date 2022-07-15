from base_page import BasePage
from fiction_page_locators import FictionPageLocators


class FictionPage(BasePage):
    def get_title(self):
        return self.driver.title

    def get_header(self):
        return self.find_element(FictionPageLocators.HEADER_LOCATORS).text
