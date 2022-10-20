from time import sleep

from pages.shop_page import ShopPage


class TestsAddPhoneToCart:

    def test_open_shop_page(self, web_browser):

        page = ShopPage(web_browser)

        assert page.get_current_url() == 'https://www.a1.by/ru/c/shop'

        sleep(3)

        print(len(page.list_stock_phone_btn.get_text()))

        page.list_stock_phone_btn[1].click()

        sleep(1)


