
from pages.webtables import WebTables
from conftest import browser


def test_modal_dialogs(browser):
    page = WebTables(browser)
    page.visit()

    assert page.first_line.get_text() == 'Cierra'

    page.btn_fn.click()
    assert page.first_line.get_text() == 'Alden'

    page.btn_fn.click()
    assert page.first_line.get_text() == 'Kierra'