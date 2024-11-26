from playwright.sync_api import sync_playwright


def choice_mobile_emulation(mobile):
    """
    - 选择模拟设备
    - param：
      - mobile：设备号（exp 'iPhone 15 Pro'）
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            **p.devices[mobile]
        )
        page = context.new_page()
        return page, browser
