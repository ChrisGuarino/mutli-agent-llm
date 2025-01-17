import pytest
from playwright.sync_api import sync_playwright

def test_example_com():
    with sync_playwright() as playwright:
        # Launch browser
        browser = playwright.chromium.launch(headless=True)  # Use headless=False to see the browser
        page = browser.new_page()

        # Navigate to the website
        page.goto("https://example.com")

        # Verify the page title contains "Example Domain"
        assert "Example Domain" in page.title()

        # Verify specific text exists on the page
        assert page.locator("h1").inner_text() == "Example Domain"

        # Take a screenshot for debugging purposes
        page.screenshot(path="example_com_test.png")

        # Close browser
        browser.close()
