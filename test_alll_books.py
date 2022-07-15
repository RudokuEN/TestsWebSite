from main_page import MainPage
from books_page import BooksPage


def test_books_is_open(driver):
    """
    Данный тест проверяет,
    точно ли загруженна страница Books
    """
    page = MainPage(driver)
    page.open()
    page.open_books_page()
    book_page = BooksPage(driver, driver.current_url)
    assert book_page.get_books_header() == 'Books'
    assert "Books" in book_page.get_title()


def test_books_name(driver):
    """
    Данный тест проверяет:
    1. Название книги
    2. Наличие изображения
    3. Заголовок страницы
    """
    page = MainPage(driver)
    page.open()
    page.open_books_page()
    book_page = BooksPage(driver, driver.current_url)
    text = book_page.find_books("Coders at Work").text
    book_page.find_books("Coders at Work").click()
    assert book_page.name_of_books() == text
    assert book_page.books_picture() is True
    assert text in book_page.get_title()
