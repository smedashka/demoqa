from components.components import WebElement
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.checkbox = WebElement(driver, 'span.rct-text')
        self.btn_options = WebElement(driver, '.rct-option.rct-option-expand-all')
