import time

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_size(browser):
    main_page = DemoQa(browser)

    main_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_navbar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert not elements_page.navbar.visible()
    browser.set_window_size(767, 1000)
    assert elements_page.navbar.visible()
    browser.set_window_size(1000, 1000)


