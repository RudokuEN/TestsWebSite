from main_page import MainPage
from fiction_page import FictionPage


def test_fiction_page(driver):
    """
    Данный тест проверяет:
    Точно ли загружена страница "Fiction"
    """
    page = MainPage(driver)
    page.open()
    page.open_fiction_page()
    fiction_page = FictionPage(driver, driver.current_url)
    assert fiction_page.get_header() == 'Fiction'
    assert "Fiction" in fiction_page.get_title()
