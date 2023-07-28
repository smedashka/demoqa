from components.components import WebElement
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.registration_form_modal = WebElement(driver, '#registration-form-modal')
        self.form = WebElement(driver, '#userForm')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.user_age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.table_row_first_name = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.table_row_last_name = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.table_row_age = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.table_row_email = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.table_row_salary = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.table_row_department = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.edit_icon = WebElement(driver, '#edit-record-4')
        self.delete_icon = WebElement(driver, '#delete-record-4')
        self.no_data_element = WebElement(driver, 'div.rt-noData')
        self.icons_delete = WebElement(driver, 'div.action-buttons > span:nth-child(2)')
        self.select_rows = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_prev = WebElement(driver, 'div.-previous > button.-btn')
        self.btn_next = WebElement(driver, 'div.-next > button.-btn')
        self.max_page_num = WebElement(driver, 'span.-pageInfo > span')
        self.current_page_num = WebElement(driver, 'div > input[type=number]')

    def fill_form(self, first_name, last_name, user_email, user_age, salary, department):
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.user_email.send_keys(user_email)
        self.user_age.send_keys(user_age)
        self.salary.send_keys(salary)
        self.department.send_keys(department)

    def add_table_row(self, first_name, last_name, user_email, user_age, salary, department):
        self.btn_add.click()
        self.fill_form(first_name, last_name, user_email, user_age, salary, department)
        self.btn_submit.click()
