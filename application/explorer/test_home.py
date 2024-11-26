from playwright.sync_api import sync_playwright

from application.explorer import config


def test_mobile_emulation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        page.set_viewport_size({"width": 1920, "height": 1080})
