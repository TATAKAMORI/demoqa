from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_submenu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btn_small_close = WebElement(driver, '#closeSmallModal')
        self.btn_large_close = WebElement(driver, '#closeLargeModal')
