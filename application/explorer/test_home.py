from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright


def test_check_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否在首页，且页面元素正常
        assert "home" in page.url
        expect(page.get_by_text("Number of Validators")).to_be_visible()
        expect(page.get_by_text("Number of Active Addresses")).to_be_visible()
        expect(page.get_by_text("Total Supply")).to_be_visible()
        expect(page.get_by_text("Average Block Time")).to_be_visible()
        browser.close()



