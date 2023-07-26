from pages.koup_elements import KoupElementsPage
from pages.koup_page import KoupPage


def test_btn_add(browser):
    main_page = KoupPage(browser)
    elements_page = KoupElementsPage(browser)

    main_page.visit()
    assert main_page.link.get_text() == "Add/Remove Elements"
    main_page.link.click()
    assert elements_page.equal_url()
    assert elements_page.btn_add.get_text() == "Add Element"
    assert elements_page.btn_add.get_dom_attribute("onclick") == "addElement()"

    for i in range(4):
        elements_page.btn_add.click()

    assert elements_page.btns_delete.check_count_elements(4)

    for elem in elements_page.btns_delete.find_elements():
        assert elem.text == "Delete"

    for i in range(4):
        elements_page.btns_delete.click()
    assert not elements_page.btns_delete.exist()









