from components.components import WebElement
from pages.base_page import BasePage


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, '#alertButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.confirm_res_text = WebElement(driver, '#confirmResult')
        self.btn_promt = WebElement(driver, '#promtButton')
        self.promt_res_text = WebElement(driver, '#promptResult')
        self.btn_timer_alert = WebElement(driver, '#timerAlertButton')

