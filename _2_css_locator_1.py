from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")

    # css selector  id , class , atrribute

    # using id
    emil_text_box = page.wait_for_selector('#email').type('swavimanbehera@.com')
    page.wait_for_timeout(4000)
    button_login = page.wait_for_selector('#enterimg').click()
    page.wait_for_timeout(4000)
    browser.close()
