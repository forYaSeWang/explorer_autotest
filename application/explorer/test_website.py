import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright


def test_check_website_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices['iPhone 11 Pro']
        )
        page = context.new_page()
        page.goto(config.UAT_EXPLORER_URL)
        # 检查是否跳转至website页面，且页面元素正常
        with page.expect_popup() as page1_info:
            page.get_by_text("Homepage").nth(1).click()
        page1 = page1_info.value
        assert '.html' in page1.url
        browser.close()
