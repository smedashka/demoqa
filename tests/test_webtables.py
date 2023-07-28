import time

from pages.webtables_page import WebTablesPage


def test_empty_table(browser):
    page = WebTablesPage(browser)

    page.visit()
    assert not page.no_data_element.exist()
    for i in page.icons_delete.find_elements():
        page.icons_delete.click()
    time.sleep(2)
    assert page.no_data_element.exist()
