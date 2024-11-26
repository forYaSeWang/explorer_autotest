import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright

mobile = 'iPhone 14 Pro'


def test_check_validators_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否跳转至validators页面，且页面元素正常
        page.locator("span:nth-child(2)").first.click()
        page.get_by_text("Validators").nth(1).click()
        print(page.url)
        assert 'validators' in page.url
        expect(page.locator("#root")).to_contain_text("Number of Validators")
        expect(page.locator("#root")).to_contain_text("Current Block Node:")
        expect(page.locator("#root")).to_contain_text("Network Staking Amount")
        expect(page.locator("#root")).to_contain_text("Unclaimed Flexible Term Rewards")
        # 选择验证节点列表中的第一个验证节点，点击进入验证者详情页面，检查页面元素
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div/span', timeout=10000)
        element.click()
        assert 'validatorDetail' in page.url
        expect(page.locator("#root")).to_contain_text("Validator Details")
        expect(page.locator("#root")).to_contain_text("Node Consensus Weight")
        expect(page.locator("#root")).to_contain_text("Staking Limit")
        expect(page.locator("#root")).to_contain_text("Total Staking Amount")
        expect(page.locator("#root")).to_contain_text("Node ID")
        # 点击复制验证者详情中的区金库地址，并通过搜索进入模块地址账户详情页，检查页面元素
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[4]/div[1]/p[2]/span[1]/span/img', timeout=10000)
        element.click()
        input_element = page.wait_for_selector(
            '//*[@id="inputSearch"]', timeout=10000)
        input_element.focus()
        page.keyboard.press("Control+V")
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[1]/div/span/span[2]/div/span', timeout=10000)
        element.click()
        assert 'address' in page.url
        expect(page.locator("#root")).to_contain_text("Address Details")
        expect(page.locator("#root")).to_contain_text("Assets")
        expect(page.locator("#root")).to_contain_text("Account Name")
        expect(page.locator("#root")).to_contain_text("Account Description")
        expect(page.locator("#root")).to_contain_text("Transactions")
        # 验证点击首页图标返回首页
        page.locator("img").first.click()
        assert "home" in page.url
        browser.close()
