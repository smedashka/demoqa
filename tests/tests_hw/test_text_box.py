from pages.textbox_page import TextboxPage


def test_text_box(browser):
    text_box_page = TextboxPage(browser)

    text_box_page.visit()
    name = 'Sherlock Holmes'
    address = 'Baker Street, 221b'
    text_box_page.full_name.send_keys(name)
    text_box_page.current_address.send_keys(address)
    text_box_page.btn_submit.click()
    assert text_box_page.name_res.get_text() == 'Name:' + name
    assert text_box_page.curr_add_res.get_text() == 'Current Address :' + address



