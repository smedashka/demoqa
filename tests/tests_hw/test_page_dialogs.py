from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btns_menu.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    main_page = DemoQa(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.btn_icon.click()
    main_page.back()
    browser.set_window_size(900, 400)
    modal_dialogs_page.forward()
    assert main_page.equal_url()
    assert main_page.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)
