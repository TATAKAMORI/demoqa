from pages.demoqa import DemoQA
from pages.modal_dialogs import modal_dialogs


def test_page_dialogs(browser):
    modal_page = modal_dialogs(browser)

    modal_page.visit()

    assert modal_page.btns.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_page = modal_dialogs(browser)
    demo_page = DemoQA(browser)

    modal_page.visit()
    browser.refresh()
    browser.icon.click()
    browser.back()
    browser.set_window_size(900, 400)

    browser.forward()
    assert demo_page.equal_url()
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
