from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_1 = (By.CSS_SELECTOR, ".breadcrumb > .active")
    BASKET_2 = (By.CSS_SELECTOR, ".page-header > h1")
