from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    page.query_selector('//input[@value="Movies"]').click()

    # page.query_selector('//input[@value="Cricket"]').click()
    # page.check()
    if page.is_checked('//input[@value="Movies"]'):
        print("passed")
    else:
        print("failed")

    page.wait_for_timeout(5000)

    browser.close()