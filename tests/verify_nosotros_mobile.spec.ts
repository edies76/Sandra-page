import { test, expect, devices } from '@playwright/test';

test.use({ ...devices['iPhone 11'] });

test('nosotros.html mobile layout verification', async ({ page }) => {
  await page.goto('nosotros.html');
  await page.screenshot({ path: 'jules-scratch/screenshot_nosotros_mobile_final.png', fullPage: true });
});
