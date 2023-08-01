import time
from selenium.webdriver import ActionChains, Keys

from pages.droppable import Droppable


# def test_drag_and_drop(browser):
#     page = Droppable(browser)
#     action_chains = ActionChains(browser)
#
#     page.visit()
#     action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
#     time.sleep(1)


def test_drag_and_drop_check_css(browser):
    page = Droppable(browser)
    action_chains = ActionChains(browser)

    page.visit()

    assert page.drop.check_css('background-color', 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    time.sleep(1)

    assert page.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')
    time.sleep(1)

    action_chains.drag_and_drop_by_offset(page.drag.find_element(), -200, 0).perform()

    time.sleep(1)
    assert page.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')

