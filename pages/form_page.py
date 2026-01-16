from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):


    def __init__(self, driver):
        self.base_page = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_page)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-Radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, '#body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')