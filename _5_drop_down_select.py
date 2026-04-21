from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    page= broswer.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    # select drop down
    # 1..ind the select location
    # select_drop_down = page.query_selector('//select[@id="Skills"]')
    # # 2..select the options
    # select_drop_down.select_option(label="AutoCAD")
    # page.wait_for_timeout(6000)
    page.select_option('//select[@id="Skills"]',label="AutoCAD")
    page.wait_for_timeout(6000)