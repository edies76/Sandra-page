from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Get the absolute path to the HTML file
    file_path = os.path.abspath('nosotros.html')
    url = f'file://{file_path}'

    # Verify header change on desktop
    page.goto(url)
    header = page.locator('#main-header')
    header.screenshot(path='jules-scratch/verification/header-screenshot.png')

    # Verify mobile layout
    page.set_viewport_size({'width': 375, 'height': 812})
    page.goto(url)
    page.screenshot(path='jules-scratch/verification/nosotros-mobile-screenshot.png', full_page=True)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
