import pytest
from selenium import webdriver
from selenium.webdriver import Keys

from pages.webtables_page import WebTablesPage


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1920, height=1080)
    yield driver
    driver.quit()

# предусловия для теста
@pytest.fixture(scope='function')
def webtable_page():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1920, height=1080)
    webtable_page = WebTablesPage(driver)
    webtable_page.visit()
    webtable_page.select_rows.click()
    webtable_page.select_rows.send_keys(Keys.PAGE_UP)
    webtable_page.select_rows.send_keys(Keys.ENTER)
    yield webtable_page
    driver.quit()
