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