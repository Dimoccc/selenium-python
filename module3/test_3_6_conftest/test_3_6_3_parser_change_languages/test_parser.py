# pytest -s -v --browser_name=chrome test_parser.py

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    
    browser.find_element('css selector', "#login_link")