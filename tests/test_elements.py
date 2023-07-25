from pages.checkbox_page import CheckboxPage
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(9)


def test_count_checkbox(browser):
    checkbox_page = CheckboxPage(browser)

    checkbox_page.visit()
    assert checkbox_page.checkbox.check_count_elements(1)
    checkbox_page.btn_options.click()
    assert checkbox_page.checkbox.check_count_elements(17)

    for elem in checkbox_page.btn_options.find_elements():
        assert elem.is_displayed()

    checkbox_page.refresh()
    assert checkbox_page.checkbox.check_count_elements(1)
