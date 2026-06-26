from types import new_class

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/Windows.html")

    page.wait_for_selector('//button[contains(text(),"click")]').click()

    page.wait_for_timeout(4000)
    # How To find thetotal pages
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)

    print(page.title())
    new_page = total_pages[1]
    # how to switch the new page
    new_page.bring_to_front()
    print(new_page.title())
    new_page.close()
    page.wait_for_timeout(4000)

    browser.close()