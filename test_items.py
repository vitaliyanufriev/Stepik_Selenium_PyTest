from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_cart(browser):
    browser.get(link)
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), f"Button 'Add to cart' missed"
