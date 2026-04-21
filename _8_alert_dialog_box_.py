from playwright.sync_api import sync_playwright
text_alert = []

def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    # page.wait_for_selector('//div[@id="OKTab"]/button').click()

    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(4000)
    # control the alert
    page.on("dialog",lambda dialog : dialog.accept())
    # for the print element
    page.on("dialog",lambda dialog : print(dialog.message))
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()


    page.wait_for_timeout(3000)

    if text_alert:
        print(text_alert[0])
    else:
        print("No alert captured")