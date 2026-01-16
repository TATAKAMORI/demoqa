import time
from pages.demoqa import DemoQA

def test_size(browser):
    demo_qa = DemoQA(browser)

    demo_qa.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)