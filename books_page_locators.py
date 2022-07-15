from selenium.webdriver.common.by import By


class BooksPageLocators:
    BOOKS_LOCATOR_HEADER = (By.CSS_SELECTOR, '.page-header > h1')
    BOOKS_LOCATOR_IMG = (By.TAG_NAME, 'img')
    BOOKS_LOCATOR_NAME_OF_BOOK = (By.TAG_NAME, 'h1')
