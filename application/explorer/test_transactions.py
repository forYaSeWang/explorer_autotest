import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright

mobile = 'iPhone 14 Pro'


def test_check_transactions_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至transactions页面，且页面元素正常
        page.locator(".header_mobile_icon___1K9QD").click()
        page.get_by_text("Transactions", exact=True).nth(1).click()
        assert 'transactions' in page.url
        expect(page.locator("#root")).to_contain_text("Tx Hash")
        expect(page.locator("#root")).to_contain_text("Status")
        expect(page.locator("#root")).to_contain_text("Tx Hash")
        expect(page.locator("#root")).to_contain_text("GasFee")
        # 选择交易列表中的第一条交易，点击进入交易详情页面，检查页面元素
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/p', timeout=10000)
        element.click()
        assert 'transactionDetail' in page.url
        expect(page.locator("#root")).to_contain_text("Transaction Details")
        expect(page.locator("#root")).to_contain_text("Block")
        expect(page.locator("#root")).to_contain_text("Status")
        expect(page.locator("#root")).to_contain_text("Timestamp")
        expect(page.locator("#root")).to_contain_text("GasLimit")
        # 验证点击首页图标返回首页
        page.locator("img").first.click()
        assert "home" in page.url
        browser.close()
