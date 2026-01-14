from components.components import WebElement
from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.check_elem = WebElement(driver, '#section1Content > p')
        self.click_elem = WebElement(driver, '#section1Heading')
        self.elem1 = WebElement(driver, '##section2Content > p:nth-child(1)')
        self.elem2 = WebElement(driver, '##section2Content > p:nth-child(2)')
        self.elem3 = WebElement(driver, '##section3Content > p')