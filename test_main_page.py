from main_page import MainPage


def test_main_page(driver):
    """
    Данный тест проверяет:
    Точно ли загружена главная страница
    """
    page = MainPage(driver)
    page.open()
    assert page.get_header_main_page() == "Welcome!"
    assert page.get_title() == 'Oscar - Sandbox'
