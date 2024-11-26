from playwright.sync_api import sync_playwright


def test_mobile_emulation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto('https://example.com')

        # 在这里编写测试步骤
