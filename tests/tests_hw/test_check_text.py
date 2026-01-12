from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA


def test_check_text(browser):

    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

def test_check_text2(browser):

    demo_qa_page = DemoQA(browser)
    page2 = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    assert page2.text2.get_text() == 'Please select an item from left to start practice.'
