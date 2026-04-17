from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser =play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    username = page.wait_for_selector('input[name="username"]').type('Admin')
    password = page.wait_for_selector('input[name="password"]').type("admin123")
    page.wait_for_selector('button[type="submit"]').click()

    page.wait_for_timeout(4000)
    browser.close()