
import os
from playwright.sync_api import sync_playwright, Page, expect

def verify_nosotros_mobile(page: Page):
    """
    This test verifies that the 'nosotros.html' page is visible on mobile and takes a full-page screenshot.
    """
    # 1. Arrange: Go to the local nosotros.html page.
    absolute_path = os.path.abspath('nosotros.html')
    page.goto(f"file://{absolute_path}")

    # 2. Set viewport to a mobile size (iPhone X).
    page.set_viewport_size({"width": 375, "height": 812})

    # 3. Assert: Check that the main heading is visible. This is a basic check to ensure the page is rendering.
    heading = page.get_by_role("heading", name="Sobre RAIZ")
    expect(heading).to_be_visible()

    # 4. Screenshot: Capture the full mobile view for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png", full_page=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        verify_nosotros_mobile(page)
        browser.close()

if __name__ == "__main__":
    main()
