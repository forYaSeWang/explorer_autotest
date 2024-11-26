import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright

mobile = 'iPhone 14 Pro'


def test_check_blocks_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
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
        # 选择区块列表中第一个块，点击跳转至区块详情页面，检查页面元素
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/p', timeout=10000)
        element.click()
        assert 'blockDetail' in page.url
        expect(page.locator("#root")).to_contain_text("Block Details")
        expect(page.locator("#root")).to_contain_text("Summary")
        expect(page.locator("#root")).to_contain_text("Block Hash")
        expect(page.locator("#root")).to_contain_text("Timestamp")
        expect(page.locator("#root")).to_contain_text("Number of Transactions")
        # 验证点击首页图标返回首页
        page.locator("img").first.click()
        assert "home" in page.url
        browser.close()
