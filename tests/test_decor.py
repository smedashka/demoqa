import time

import pytest

from pages.demoqa import DemoQa
from pages.radio_button import RadioButton


@pytest.mark.skip
def test_check_header(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.header_elem.check_count_elements(6)

    for i in page.header_elem.find_elements():
        assert not i.text == ''


# @pytest.mark.skipif(True, reason='просто пропуск')
def test_radio_button(browser):
    page = RadioButton(browser)

    if page.code_status() != 200:
        pytest.skip()

    page.visit()

    page.btn_yes.click_force()
    assert page.text_success.get_text() == 'Yes'

    page.btn_impressive.click_force()
    assert page.text_success.get_text() == 'Impressive'

    assert 'disabled' in page.btn_no.get_dom_attribute('class')

