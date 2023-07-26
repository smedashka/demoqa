from components.components import WebElement
from pages.base_page import BasePage


class KoupPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.link = WebElement(driver, '#content > ul > li:nth-child(2) > a')
