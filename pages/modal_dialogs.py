from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_menu = WebElement(driver, 'div.accordion > div:nth-child(3) > div > ul > li')
