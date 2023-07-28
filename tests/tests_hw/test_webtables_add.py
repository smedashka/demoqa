import time

from pages.webtables_page import WebTablesPage


def test_login_form_validate(webtable_page: WebTablesPage):
    assert not webtable_page.btn_prev.is_enabled()
    assert webtable_page.btn_prev.get_dom_attribute('disabled')

    webtable_page.add_table_row('Jonathan', 'Small', 'j_small@mail.com', '40', '10000', 'Criminal')
    webtable_page.add_table_row('John', 'Watson', 'j_watson@mail.com', '30', '80000', 'Medical')
    webtable_page.add_table_row('G.', 'Lestrade', 'g_lestrade@mail.com', '33', '90000', 'Detective')

    assert webtable_page.max_page_num.get_text() == '2'
    assert webtable_page.btn_next.is_enabled()

    webtable_page.btn_next.click()
    assert webtable_page.current_page_num.get_dom_attribute('value') == '2'

    webtable_page.btn_prev.click()
    assert webtable_page.current_page_num.get_dom_attribute('value') == '1'



