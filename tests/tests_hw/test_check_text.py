from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_footer(browser):
    main_page = DemoQa(browser)

    main_page.visit()
    assert main_page.equal_url()
    assert main_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_elem(browser):
    main_page = DemoQa(browser)
    elem_page = ElementsPage(browser)

    main_page.visit()
    assert main_page.equal_url()
    main_page.btn_elements.click()
    assert elem_page.equal_url()
    assert elem_page.main_text.get_text() == 'Please select an item from left to start practice.'











