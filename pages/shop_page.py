from pages.base_page import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement


class ShopPages(WebPage):

    def __init__(self, web_driver):
        url = 'https://www.a1.by/ru/c/shop'
        super().__init__(web_driver, url)

    # list of start page selectorss
    list_stock_phone_btn = ManyWebElements(xpath="//*[@id='promo-product-button_0']")
    list_phone_summary = ManyWebElements(xpath="//*[@id='promo-product-button_0']/../..//h3")
    cookie_btn = WebElement(css_selector=".cookie-panel-button")

    # list smartphone page selectors
    page_h1 = WebElement(xpath="//h1")
    payment_options_btn = WebElement(xpath='//*[@class="live-filter-controls"]')
    list_payment_options = ManyWebElements(xpath='//li/div[@class="value"]')
    buy_btn = WebElement(xpath='//*[@class="live-filter-content-item active"]//button')
    pay_in_mounth = WebElement(xpath='//*[@class="live-filter-content-item active"]//span[@class="h h--4"]')

    # list login screen selectors
    radio_passwrd_btn = WebElement(xpath="//span[2]/label")
    enter_phone_filed = WebElement(css_selector='#itelephone_new')
    enter_password = WebElement(css_selector='#ipassword')

