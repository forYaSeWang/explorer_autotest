import re

from playwright.sync_api import expect

from application.explorer import config

from playwright.sync_api import sync_playwright

mobile = 'iPhone 14 Pro'


def test_check_me_network():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至me_network页面，且页面元素正常
        page.get_by_role("tab", name="Solutions").locator("span").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("tabpanel").get_by_text("ME Network").click()
        page1 = page1_info.value
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("Modular blockchain multi-chain fusion network")
        assert 'network' in page1.url
        browser.close()


def test_check_me_id():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至me_network页面，且页面元素正常
        page.get_by_role("tab", name="Solutions").locator("span").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("tabpanel").get_by_text("ME ID").click()
        page1 = page1_info.value
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("Next-Generation Personal Sovereign Identity")
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("ME ID")
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("Basic Working Mode")
        assert 'id' in page1.url
        browser.close()


def test_check_me_pass():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至me_pass页面，且页面元素正常
        page.get_by_role("tab", name="Solutions").locator("span").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("tabpanel").get_by_text("ME Pass").click()
        page1 = page1_info.value
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("ME Pass")
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("Next-Generation Global Financial Gateway")
        assert 'mePass' in page1.url
        browser.close()


def test_check_me_earth():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至me_earth页面，且页面元素正常
        page.get_by_role("tab", name="Solutions").locator("span").click()
        with page.expect_popup() as page3_info:
            page.get_by_role("tabpanel").get_by_text("Meta Earth").click()
        page1 = page3_info.value
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text("Recreating a Parallel World")
        expect(page1.locator("#MEInnerLayoutBody")).to_contain_text(
            "Meta Earth is based on a value network — ME (Meta Earth) Network, and aims to promote the improvement of the Human Happiness Index and the sustainable development of the ecological environment.")
        assert 'earth' in page1.url
        browser.close()


def test_check_validator():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至me_validator页面，且页面元素正常
        page.get_by_role("tab", name="Ecosystem").locator("span").click()
        page.get_by_role("tabpanel").get_by_text("Validator").click()
        expect(page.locator("#root")).to_contain_text("Validators")
        expect(page.locator("#root")).to_contain_text("Number of Validators")
        expect(page.locator("#root")).to_contain_text("Network Staking Amount")
        expect(page.locator("#root")).to_contain_text("Unclaimed Flexible Term Rewards")
        assert 'validators' in page.url
        browser.close()


def test_check_token_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至token页面，且页面元素正常
        page.get_by_role("tab", name="Solutions").locator("span").click()
        with page.expect_popup() as page2_info:
            page.get_by_role("tabpanel").get_by_text("Token").click()
        page2 = page2_info.value
        expect(page2.locator("#MEInnerLayoutBody")).to_contain_text("Meta Earth Network Native Token")
        expect(page2.locator("#MEInnerLayoutBody")).to_contain_text("Learn about MEC")
        assert 'token' in page2.url
        browser.close()
