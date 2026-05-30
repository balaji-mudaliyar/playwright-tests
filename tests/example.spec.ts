import { test, expect } from '@playwright/test';

test('homepage has Playwright title', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Playwright/);
});
