from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_content = WebElement(driver, 'div.fade.modal.show > div > div')
        self.modal_first_name = WebElement(driver, '#firstName')
        self.modal_last_name = WebElement(driver, '#lastName')
        self.modal_email = WebElement(driver, '#userEmail')
        self.modal_age = WebElement(driver, '#age')
        self.modal_salary = WebElement(driver, '#salary')
        self.modal_department = WebElement(driver, '#department')
        self.btn_modal_submit = WebElement(driver, '#submit')
        self.btn_edit1 = WebElement(driver, '#edit-record-1')
        self.btn_edit2 = WebElement(driver, '#edit-record-2')
        self.btn_edit3 = WebElement(driver, '#edit-record-3')
        self.btn_delete = WebElement(driver, '#delete-record-1')
        self.btn_delete2 = WebElement(driver, '#delete-record-2')
        self.btn_delete3 = WebElement(driver, '#delete-record-3')


