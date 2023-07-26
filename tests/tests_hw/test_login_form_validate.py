from pages.form_page import FormPage


def test_login_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute(
        'pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    assert not form_page.form.get_dom_attribute('class') == 'was-validated'
    form_page.btn_submit.click()
    assert form_page.form.get_dom_attribute('class') == 'was-validated'
