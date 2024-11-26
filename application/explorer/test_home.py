from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright

mobile = 'iPhone 14 Pro'


def test_check_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否在首页，且页面元素正常
        assert "home" in page.url
        expect(page.get_by_text("Number of Validators")).to_be_visible()
        expect(page.get_by_text("Number of Active Addresses")).to_be_visible()
        expect(page.get_by_text("Total Supply")).to_be_visible()
        expect(page.get_by_text("Average Block Time")).to_be_visible()
        # 首页最新区块点击,跳转区块详情页
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[1]/div/p[2]', timeout=10000)
        element.click()
        assert 'blockDetail' in page.url
        # 返回首页
        page.locator("img").first.click()
        # More Blocks跳转验证
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[2]', timeout=10000)
        element.click()
        assert 'blocks' in page.url
        # 返回首页
        page.locator("img").first.click()
        # More transactions跳转验证
        element = page.wait_for_selector(
            '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[4]/div/div[1]/div', timeout=10000)
        element.click()
        assert 'transactions' in page.url
        browser.close()
