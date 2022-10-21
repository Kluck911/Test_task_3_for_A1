from time import sleep
import random

from pages.shop_page import ShopPages


class TestsA1Shop:

    def test_add_stock_rnd_phone_to_cart(self, web_browser):

        page = ShopPages(web_browser)
        assert page.get_current_url() == 'https://www.a1.by/ru/c/shop', 'shop page url error'

        rnd_number = random.randint(0, len(page.list_stock_phone_btn.get_text())-1)  # random number for phone block
        page.cookie_btn.click()  # close cookie message
        start_page_phone_summary = page.list_phone_summary.get_text()[rnd_number]  # save smartphone summary
        page.list_stock_phone_btn[rnd_number].click()
        print(start_page_phone_summary)
        assert page.get_current_url() == 'https://www.a1.by/ru/shop/phones/smartphones*'
