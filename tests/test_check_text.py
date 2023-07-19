from pages.elements_page import ElementsPage


def test_check_text(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.text.get_text() == 'Elements'
    

