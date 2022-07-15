from base_page import BasePage
from basket_page_locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Данный класс реализует методы для работы
    с элементами ка странице "Корзина"
    """

    def get_title(self):
        return self.driver.title

    def get_text_basket_1(self):
        return self.find_element(BasketPageLocators.BASKET_1).text

    def get_text_basket_2(self):
        return self.find_element(BasketPageLocators.BASKET_2).text

    def get_text_basket_empty(self):
        return self.find_element(BasketPageLocators.BASKET_IS_EMPTY).text
