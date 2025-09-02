import os

def test_example(page):
    page.goto(os.getenv("Url"))
    page.click("#app > div > div > div.home-body > div > div:nth-child(1)")
    page.wait_for_timeout(100)
    page.click("#item-0")
    page.fill("#userName", os.getenv("UserName"))
    page.fill("#userEmail", os.getenv("UserEmail"))
    page.fill("#currentAddress", os.getenv("CurrentAddress"))
    page.fill("#permanentAddress", os.getenv("PermanentAddress"))
    page.click("#submit")
    page.wait_for_selector("#name")

    userName = page.inner_text("#name")
    userEmail = page.inner_text("#email")

    if os.getenv("UserName") in userName and os.getenv("UserEmail") in userEmail:
        print("ok")
    else:
        print("not ok")