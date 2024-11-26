import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright


def test_check_validators_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否跳转至validators页面，且页面元素正常
        page.locator("span:nth-child(2)").first.click()
        page.get_by_text("Validators").nth(1).click()
        assert 'validators' in page.url
        expect(page.locator("#root")).to_contain_text("Number of Validators")
        expect(page.locator("#root")).to_contain_text("Current Block Node:")
        expect(page.locator("#root")).to_contain_text("Network Staking Amount")
        expect(page.locator("#root")).to_contain_text("Unclaimed Flexible Term Rewards")
        #
        page.evaluate('window.scrollBy(0, window.innerHeight)')
        element = page.query_selector('//xpath_expression')
        element.click()
        # 验证点击首页图标返回首页
        page.locator("img").first.click()
        assert "homes" in page.url
        browser.close()
