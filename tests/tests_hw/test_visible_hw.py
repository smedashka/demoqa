import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordian_page = Accordion(browser)

    accordian_page.visit()
    assert accordian_page.card_first_text.visible()
    accordian_page.card_first_header.click()
    time.sleep(2)
    assert not accordian_page.card_first_text.visible()


def test_visible_accordion_default(browser):
    accordian_page = Accordion(browser)

    accordian_page.visit()
    assert not accordian_page.card_second_text_first.visible()
    assert not accordian_page.card_second_text_second.visible()
    assert not accordian_page.card_third_text.visible()


