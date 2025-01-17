from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    # Example: Interact with the page
    page.fill("input[name='username']", "your_username")
    page.fill("input[name='password']", "your_password")
    page.click("button[type='submit']")

    # Take a screenshot
    page.screenshot(path="screenshot.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
