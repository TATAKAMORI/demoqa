import time
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert browser.title == 'DEMOQA'

    assert modal_page.btn_small.exist()
    assert modal_page.btn_large.exist()

    modal_page.btn_small.click()
    assert modal_page.modal.exist()
    time.sleep(2)
    assert modal_page.btn_small_close.exist()
    modal_page.btn_small_close.click_force()
    assert not modal_page.modal.exist()

