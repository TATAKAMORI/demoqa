import time
from pages.alerts import Alerts



def test_check_alert(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()

    assert alerts_page.timer_alert_button.exist()
    alerts_page.timer_alert_button.click()
    time.sleep(5)
    alerts_page.alert().accept()
    assert not alerts_page.alert()
    time.sleep(2)