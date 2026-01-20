from pages.text_box import TextBox
import time



def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.name.send_keys('text1')
    text_box_page.current_address.send_keys('text2')
    text_box_page.submit_button.click_force()

    assert text_box_page.name2.get_text() == 'Name:text1'
    assert text_box_page.address2.get_text() == 'Current Address :text2'



