from application.explorer import config

from playwright.sync_api import sync_playwright, expect

mobile = 'iPhone 14 Pro'


def test_check_address_disclosure_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否跳转至公式地址页面，且页面元素正常
        page.get_by_role("tab", name="Ecosystem").locator("span").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("tabpanel").get_by_text("Address Disclosure").click()
        page1 = page1_info.value
        expect(page1.get_by_role("paragraph")).to_contain_text("Meta Earth Governance Address")
        expect(page1.locator("#scroll-wrapper")).to_contain_text("Governance Address")
        expect(page1.locator("#scroll-wrapper")).to_contain_text("Node Address")
        assert 'governAddress' in page1.url
        browser.close()
