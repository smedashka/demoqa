from components.components import WebElement
from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.card_first_text = WebElement(driver, '#section1Content > p ')
        self.card_first_header = WebElement(driver, '#section1Heading')
        self.card_second_text_first = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.card_second_text_second = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.card_third_text = WebElement(driver, '#section3Content > p')
