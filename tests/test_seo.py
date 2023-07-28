import time

import pytest

from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
from pages.alerts import Alerts


# def test_check_title(browser):
#     main_page = DemoQa(browser)
#
#     main_page.visit()
#     assert main_page.get_title() == 'DEMOQA'
#     # assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
