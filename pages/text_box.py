from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress.form-control')
        self.submit_button = WebElement(driver, '#submit')
        self.name2 = WebElement(driver, '#name')
        self.address2 = WebElement(driver, '#currentAddress.mb-1')