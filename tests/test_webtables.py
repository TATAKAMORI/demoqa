import time
from pages.webtables import WebTables

def test_web_tables(browser):
    page = WebTables(browser)
    page.visit()
    time.sleep(2)


    page.btn_add.click()
    time.sleep(2)
    assert page.modal_content.visible()


    page.btn_modal_submit.click()
    time.sleep(2)
    assert page.modal_content.visible()

    page.modal_first_name.send_keys("Mikhail")
    page.modal_last_name.send_keys("Bukin")
    page.modal_email.send_keys("test@ttt.com")
    page.modal_age.send_keys("30")
    page.modal_salary.send_keys("99999")
    page.modal_department.send_keys("IT")

    page.btn_modal_submit.click()
    time.sleep(2)

    assert not page.modal_content.exist()


    page.btn_edit1.click()
    time.sleep(2)

    assert page.modal_content.visible()

    page.modal_first_name.clear()
    page.modal_first_name.send_keys("Test")
    page.btn_modal_submit.click()
    time.sleep(2)

    assert page.btn_delete.exist()
    page.btn_delete.click()
    time.sleep(2)
