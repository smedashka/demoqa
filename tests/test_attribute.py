from pages.textbox_page import TextboxPage


def test_placeholder(browser):
    textbox_page = TextboxPage(browser)

    textbox_page.visit()
    assert textbox_page.full_name.get_dom_attribute('placeholder') == 'Full Name'
