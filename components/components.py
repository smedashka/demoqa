from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int):
        return len(self.find_elements()) == count

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return self.find_element().text

    def visible(self):
        return self.find_element().is_displayed()
