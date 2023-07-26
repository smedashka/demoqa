import time

from pages.webtables_page import WebTablesPage


def test_login_form_validate(browser):
    page = WebTablesPage(browser)

    page.visit()
    assert page.btn_add.get_text() == 'Add'
    page.btn_add.click()
    assert page.registration_form_modal.exist()
    page.btn_submit.click()
    assert page.form.get_dom_attribute('class') == 'was-validated'

    first_name = 'Sherlock'
    last_name = 'Holmes'
    user_email = 'sherlock_holmes@mail.com'
    user_age = '33'
    salary = '50000'
    department = 'Special'

    page.first_name.send_keys(first_name)
    page.last_name.send_keys(last_name)
    page.user_email.send_keys(user_email)
    page.user_age.send_keys(user_age)
    page.salary.send_keys(salary)
    page.department.send_keys(department)
    page.btn_submit.click()

    assert_table_row(page, first_name, last_name, user_email, user_age, salary, department)

    page.edit_icon.click()
    assert page.registration_form_modal.exist()
    assert page.first_name.get_dom_attribute('value') == first_name
    assert page.last_name.get_dom_attribute('value') == last_name
    assert page.user_email.get_dom_attribute('value') == user_email
    assert page.user_age.get_dom_attribute('value') == user_age
    assert page.salary.get_dom_attribute('value') == salary
    assert page.department.get_dom_attribute('value') == department

    page.first_name.clear()
    new_first_name = 'Mycroft'
    page.first_name.send_keys(new_first_name)
    page.btn_submit.click()
    assert_table_row(page, new_first_name, last_name, user_email, user_age, salary, department)

    page.delete_icon.click()
    assert_table_row(page, ' ', ' ', ' ', ' ', ' ', ' ')


def assert_table_row(page, first_name, last_name, user_email, user_age, salary, department):
    assert page.table_row_first_name.get_text() == first_name
    assert page.table_row_last_name.get_text() == last_name
    assert page.table_row_email.get_text() == user_email
    assert page.table_row_age.get_text() == user_age
    assert page.table_row_salary.get_text() == salary
    assert page.table_row_department.get_text() == department
