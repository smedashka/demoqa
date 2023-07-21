from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btns_menu.check_count_elements(5)
