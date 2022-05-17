from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    print(browser)
    browser.get(link)
    add_to_cart = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(add_to_cart) > 0, \
               'Not found!'