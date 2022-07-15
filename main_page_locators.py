from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_WELCOME = (By.XPATH, "//h2[text()='Welcome!']")
    BOOKS_LOCATOR = (By.CSS_SELECTOR,
                     'a[href="/en-gb/catalogue/category/books_2/"]')
    FICTION_CLOTHING_LOCATORS = (By.CSS_SELECTOR,
                                 'a[href='
                                 '"/en-gb/catalogue/category/clothing_1/"]')
    FICTION_LOCATORS = (By.CSS_SELECTOR,
                        '.side_categories > ul a['
                        'href="/en-gb/catalogue/category/books/fiction_3/"]')
    VIEW_BASKET = (By.CSS_SELECTOR,
                   'span > .btn-default[href="/en-gb/basket/"]')
