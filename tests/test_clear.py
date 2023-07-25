import time

from pages.textbox_page import TextboxPage


def test_clear(browser):
    textbox_page = TextboxPage(browser)

    textbox_page.visit()
    textbox_page.full_name.send_keys('bla bla bla')
    time.sleep(2)
    textbox_page.full_name.clear()
    time.sleep(2)
    assert textbox_page.full_name.get_text() == ''
