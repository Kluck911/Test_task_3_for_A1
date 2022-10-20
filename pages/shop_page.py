from pages.base_page import WebPage
from pages.elements import ManyWebElements



class ShopPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://www.a1.by/ru/c/shop'
        super().__init__(web_driver, url)

    list_stock_phone_btn = ManyWebElements(xpath="//*[@id='promo-product-button_0']")
    btn = ''

