from components.components import WebElement
from pages.base_page import BasePage


class modal_dialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_submenu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul')
        self.btns = WebElement(driver, 'btn')
        self.icon = WebElement(driver, '#app > header > a > img')