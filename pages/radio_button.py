from components.components import WebElement
from pages.base_page import BasePage


class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.btn_yes = WebElement(driver, '#yesRadio')
        self.btn_impressive = WebElement(driver, '#impressiveRadio')
        self.btn_no = WebElement(driver, '#noRadio')
        self.text_success = WebElement(driver, 'span.text-success')