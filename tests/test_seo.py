from pages.demoqa import DemoQa


def test_check_title(browser):
    main_page = DemoQa(browser)

    main_page.visit()
    assert main_page.get_title() == 'DEMOQA'
    # assert browser.title == 'DEMOQA'
