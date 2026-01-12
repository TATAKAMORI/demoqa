from selenium.common import NoSuchElementException

from components.components import WebElement
from pages.base_page import BasePage

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text2 = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')


