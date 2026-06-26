from pydoc import browse, pager

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.redbus.in/")
    # give all the cookies
    my_cookies= page.context.cookies()
    print(my_cookies)
    # clear all the cookies
    page.context.clear_cookies()

    new_cookies = {
        'name':'swaviman',
        'udid' : 'krn98fhe'

    }
    # To pass the newcookies to the page
    page.context.add_cookies([new_cookies])
   #  how to take the screeenshort
   page.screenshot(path='test.png')


