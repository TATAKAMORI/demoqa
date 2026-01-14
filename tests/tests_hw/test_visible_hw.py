from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    accordion_page.check_elem.visible()
    accordion_page.check_elem.click()
    time.sleep(2)
    assert not accordion_page.check_elem.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert not accordion_page.elem1.visible()
    assert not accordion_page.elem2.visible()
    assert not accordion_page.elem3.visible()

