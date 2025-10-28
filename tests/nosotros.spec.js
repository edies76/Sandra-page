const { test, expect } = require('@playwright/test');

test.describe('Nosotros Page Mobile Layout', () => {
  test.use({
    viewport: { width: 375, height: 812 }, // iPhone X viewport
  });

  test('should have a responsive layout on mobile', async ({ page }) => {
    // Navigate to the nosotros page
    await page.goto('nosotros.html');

    // Take a screenshot of the page
    await page.screenshot({ path: 'nosotros-mobile-screenshot.png', fullPage: true });

    // Add an assertion to check if the main heading is visible
    const mainHeading = page.locator('h1', { hasText: 'Sobre RAIZ' });
    await expect(mainHeading).toBeVisible();
  });
});
