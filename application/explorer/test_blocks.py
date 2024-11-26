import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright


def test_check_blocks_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否跳转至blocks页面，且页面元素正常
        page.locator(".header_mobile_icon___1K9QD").click()

        page.locator("div").filter(has_text=re.compile(r"^Blocks$")).nth(1).click()
        assert "blocks" in page.url
        expect(page.locator("#root")).to_contain_text("Block Hash")
        expect(page.locator("#root")).to_contain_text("Block Rewards")
        expect(page.locator("#root")).to_contain_text("Block Hash")
        # 验证点击首页图标返回首页
        page.locator("img").first.click()
        assert "homes" in page.url
        browser.close()



