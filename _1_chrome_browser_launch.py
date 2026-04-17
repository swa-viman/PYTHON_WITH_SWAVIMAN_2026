
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser= p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    print("chrome successfully open")
    print(page.title())
    page.wait_for_timeout(5000)
    browser.close()