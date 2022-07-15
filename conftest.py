import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver_path =\
        "driver_Firefox_Selenium/geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driver_path)
    yield driver
    driver.quit()
