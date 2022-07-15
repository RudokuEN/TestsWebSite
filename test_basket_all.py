from main_page import MainPage
from basket_page import BasketPage


def test_basket(driver):
    """
    Данный тест проверяет:
    1. Точно ли загружена страница корзины
    2. Пустоту корзины
    """
    page = MainPage(driver)
    page.open()
    page.open_basket()
    basket_page = BasketPage(driver, driver.current_url)
    assert "Basket" in basket_page.get_title()
    assert basket_page.get_text_basket_1() == "Basket"
    assert basket_page.get_text_basket_2() == "Basket"
    assert basket_page.get_text_basket_empty() ==\
           "Your basket is empty. Continue shopping"
