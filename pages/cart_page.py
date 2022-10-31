from pages.base_page import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement


class CartPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://www.a1.by/ru/shop/phones/smartphones'

        super().__init__(web_driver, url)

    # list cart selectors
    cart_page_h2 = WebElement(xpath='//h2')
    cart_phone_summary = WebElement(xpath='//h4[@class="h h--4 payment-header"]')
    cart_phone_descr = ManyWebElements(css_selector=".payment-format-selection-radio--active")
