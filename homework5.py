from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

try:
    page.goto("https://demoqa.com/", timeout=10000)
    page.click("#app > div > div > div.home-body > div > div:nth-child(1)")
    page.wait_for_timeout(100)
    page.click("#item-0")
    page.fill("#userName", "Wozewald")
    page.fill("#userEmail", "Wozewald@gmail.com")
    page.fill("#currentAddress", "213213`")
    page.fill("#permanentAddress", "32141234324")
    page.click("#submit")
    page.wait_for_selector("#name")

    userName = page.inner_text("#name")
    userEmail = page.inner_text("#email")

    if "Wozewald" in userName and "Wozewald@gmail.com" in userEmail:
        print("ok")
    else:
        print ("not ok")

except Exception as e:
    print(f"Ошибка {e}")

finally:
    browser.close()
    playwright.stop()