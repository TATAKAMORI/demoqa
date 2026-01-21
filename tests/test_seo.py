from pages.demoqa import DemoQA
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    assert browser.title == "DEMOQA"


def test_seo(browser):
    demoqa_page = DemoQA(browser)

    demoqa_page.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
