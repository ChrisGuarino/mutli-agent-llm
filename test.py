from playwright.sync_api import sync_playwright

def launch_browser():
    user_data_dir = "persistent_data"
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False
    )
    page = browser.pages[0] if browser.pages else browser.new_page()

    print("Browser launched. Please log in manually.")
    input("Press Enter once you have logged into the website...")
    return page, browser, playwright

launch_browser()