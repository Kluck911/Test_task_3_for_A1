from pages.base_page import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement


class SmartphonePage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://www.a1.by/ru/shop/phones/smartphones'

        super().__init__(web_driver, url)


    # list smartphone page selectors
    smart_page_h1 = WebElement(xpath="//h1")
    payment_options_btn = WebElement(xpath='//*[@class="live-filter-controls"]')
    list_payment_options = ManyWebElements(xpath='//li/div[@class="value"]')
    buy_btn = WebElement(xpath='//*[@class="live-filter-content-item active"]//button')
    pay_in_mounth = WebElement(xpath='//*[@class="live-filter-content-item active"]//span[@class="h h--4"]')

