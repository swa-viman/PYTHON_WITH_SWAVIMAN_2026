from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # use relative xpath
    # use attribute
    user_element = page.wait_for_selector('//input[@name="username"]').type("Admin")
    password_element = page.wait_for_selector('//input[@type="password"]').type('admin123')

    login = page.wait_for_selector('//button[@type="submit"]').click()

    page.wait_for_timeout(4000)

    # text = //tagname[text()="text"]

    page.wait_for_selector('//p[text()="Forgot your password? "]').click()

    page.wait_for_timeout(4000)

    # contains
    # attributes = //tagname[contains(@attribute,"value")]
    # text = //tagname[contains(text(),"forgot your")]
