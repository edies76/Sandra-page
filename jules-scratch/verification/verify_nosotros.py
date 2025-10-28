
import os
from playwright.sync_api import sync_playwright, Page, expect

def verify_nosotros_mobile(page: Page):
    """
    This test verifies that the 'nosotros.html' page is mobile-friendly and has a 'Back to Home' button.
    """
    # 1. Arrange: Go to the local nosotros.html page.
    absolute_path = os.path.abspath('nosotros.html')
    page.goto(f"file://{absolute_path}")

    # 2. Set viewport to a mobile size.
    page.set_viewport_size({"width": 375, "height": 667})

    # 3. Assert: Check that the "Back to Home" button is visible.
    back_button = page.get_by_role("link", name="← Volver a la página principal")
    expect(back_button).to_be_visible()

    # 4. Assert: Check that the main content is visible and laid out vertically.
    # We can check the location of two sections to ensure they are not side-by-side.
    crianza_section = page.locator("section:has-text('Crianza Respetuosa')")
    prevencion_section = page.locator("section:has-text('Prevención del abuso sexual infantil')")

    crianza_box = crianza_section.bounding_box()
    prevencion_box = prevencion_section.bounding_box()

    # In a mobile view, the top of the second section should be below the bottom of the first section.
    assert crianza_box['y'] + crianza_box['height'] < prevencion_box['y']

    # 5. Screenshot: Capture the mobile view for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        verify_nosotros_mobile(page)
        browser.close()

if __name__ == "__main__":
    main()
