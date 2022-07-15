from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_page import BasePage
from books_page_locators import BooksPageLocators


class BooksPage(BasePage):
    """
    Данный класс реализует методы для работы
    с элементами ка странице "Книга"
    """

    def get_title(self):
        return self.driver.title

    def get_books_header(self):
        return self.find_element(BooksPageLocators.BOOKS_LOCATOR_HEADER).text

    def find_books(self, name_books):
        try:
            element = self.driver.find_element(By.LINK_TEXT, name_books)
            return element
        except TimeoutException:
            return None

    def books_picture(self):
        return bool(self.find_element(BooksPageLocators.BOOKS_LOCATOR_IMG))

    def name_of_books(self):
        return self.find_element(
            BooksPageLocators.BOOKS_LOCATOR_NAME_OF_BOOK).text
