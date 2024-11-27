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
        page.get_by_role("tab", name="Ecosystem").locator("span").click()
        with page.expect_popup() as page2_info:
            page.get_by_role("tabpanel").get_by_text("Token").click()
        page2 = page2_info.value
        expect(page2.locator("#MEInnerLayoutBody")).to_contain_text("Meta Earth Network Native Token")
        expect(page2.locator("#MEInnerLayoutBody")).to_contain_text("Learn about MEC")
        assert 'token' in page2.url
        browser.close()


def test_check_twitter_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至twitter页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("tabpanel").get_by_text("Twitter").click()
        page1 = page1_info.value
        assert 'x' in page1.url
        browser.close()


def test_check_discord_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至discord页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page2_info:
            page.get_by_role("tabpanel").get_by_text("Discord").click()
        page2 = page2_info.value
        expect(page2.get_by_role("button")).to_contain_text("接受邀请")
        expect(page2.locator("#app-mount")).to_contain_text("您已被邀请加入")
        assert 'discord' in page2.url
        browser.close()


def test_check_telegram_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至telegram页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page3_info:
            page.get_by_role("tabpanel").get_by_text("Telegram").click()
        page3 = page3_info.value
        expect(page3.locator("body")).to_contain_text("View in Telegram")
        assert 't.me' in page3.url
        browser.close()


def test_check_mirror_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至mirror页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page4_info:
            page.get_by_role("tabpanel").get_by_text("Mirror").click()
        page4 = page4_info.value
        assert 'mirror' in page4.url
        browser.close()


def test_check_medium_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至medium页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page5_info:
            page.get_by_role("tabpanel").get_by_text("Medium").click()
        page5 = page5_info.value
        expect(page5.locator("#root")).to_contain_text("WriteSign upSign in")
        expect(page5.get_by_role("main")).to_contain_text("Follow")
        expect(page5.get_by_role("navigation")).to_contain_text("Home")
        expect(page5.get_by_role("navigation")).to_contain_text("Lists")
        assert 'medium' in page5.url
        browser.close()


def test_check_linkedln_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至linkedln页面，且页面元素正常
        page.get_by_role("tab", name="Community").locator("span").click()
        with page.expect_popup() as page6_info:
            page.get_by_role("tabpanel").get_by_text("LinkedIn").click()
        page6 = page6_info.value
        expect(page6.frame_locator("iframe[title=\"Sign in with Google Dialog\"]").get_by_label(
            "使用 Google 账号登录")).to_contain_text("使用您的 Google 账号登录LinkedIn")
        assert 'linkedin' in page6.url
        browser.close()


def test_check_github_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至github页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        with page.expect_popup() as page7_info:
            page.get_by_role("tabpanel").get_by_text("Github↗").click()
        page7 = page7_info.value
        expect(page7.locator("#code-tab")).to_contain_text("Code")
        expect(page7.locator("#issues-tab")).to_contain_text("Issues")
        expect(page7.locator("#pull-requests-tab")).to_contain_text("Pull requests")
        assert 'github' in page7.url
        browser.close()


def test_check_white_paper_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至white_paper页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        page.get_by_role("tab", name="About").locator("span").click()
        with page.expect_popup() as page8_info:
            page.get_by_role("tabpanel").get_by_text("White Paper ↗").click()
        page8 = page8_info.value
        expect(page8.locator("h1")).to_contain_text("👋Welcome")
        expect(page8.get_by_role("banner")).to_contain_text("White Paper V1.0")
        assert 'white-paper' in page8.url
        browser.close()


def test_check_blog_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至blog页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        page.get_by_role("tab", name="About").locator("span").click()
        with page.expect_popup() as page9_info:
            page.get_by_role("tabpanel").get_by_text("Blog").click()
        page9 = page9_info.value
        expect(page9.locator("#MEInnerLayoutBody")).to_contain_text("Popular Blogs")
        expect(page9.locator("#MEInnerLayoutBody")).to_contain_text("Want to read more?")
        assert 'blog' in page9.url
        browser.close()


def test_check_faq_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至faq页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        page.get_by_role("tab", name="About").locator("span").click()
        with page.expect_popup() as page10_info:
            page.get_by_role("tabpanel").get_by_text("FAQ").click()
        page10 = page10_info.value
        expect(page10.locator("#MEInnerLayoutBody")).to_contain_text("+What is ZK Rollup?")
        expect(page10.locator("#MEInnerLayoutBody")).to_contain_text("What is Optimistic Rollup?")
        assert 'faq' in page10.url
        browser.close()


def test_check_team_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至team页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        page.get_by_role("tab", name="About").locator("span").click()
        with page.expect_popup() as page11_info:
            page.get_by_role("tabpanel").get_by_text("Team").click()
        page11 = page11_info.value
        expect(page11.locator("#MEInnerLayoutBody")).to_contain_text("About Us")
        expect(page11.locator("#MEInnerLayoutBody")).to_contain_text("Our Team")
        assert 'team' in page11.url
        browser.close()


def test_check_careers_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        page.goto(config.EXPLORER_URL)
        # 检查是否跳转至careers页面，且页面元素正常
        page.get_by_role("tab", name="Developers").locator("span").click()
        page.get_by_role("tab", name="About").locator("span").click()
        with page.expect_popup() as page12_info:
            page.get_by_role("tabpanel").get_by_text("Careers").click()
        page12 = page12_info.value
        expect(page12.locator("#MEInnerLayoutBody")).to_contain_text("We are hiring talent")
        expect(page12.locator("#MEInnerLayoutBody")).to_contain_text("Apply")
        expect(page12.locator("#MEInnerLayoutBody")).to_contain_text("See more positions")
        assert 'job' in page12.url
        browser.close()
