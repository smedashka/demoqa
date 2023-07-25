from components.components import WebElement
from pages.base_page import BasePage


class TextboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.name_res = WebElement(driver, '#name')
        self.curr_add_res = WebElement(driver, 'p#currentAddress')
