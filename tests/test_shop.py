from time import sleep
import random

from pages.shop_page import ShopPages



class TestsA1Shop:

    def test_add_stock_rnd_phone_to_cart(self, web_browser):

        # Step 1
        page = ShopPages(web_browser)
        assert page.get_current_url() == 'https://www.a1.by/ru/c/shop', 'shop page url error'

        # Step 2
        rnd_number = random.randint(0, len(page.list_stock_phone_btn.get_text())-1)  # random number for phone block
        page.cookie_btn.click()  # close cookie message
        start_page_phone_summary = page.list_phone_summary.get_text()[rnd_number]  # save smartphone summary
        page.list_stock_phone_btn[rnd_number].click()

        assert 'https://www.a1.by/ru/shop/phones/smartphones' in page.get_current_url()  # check url
        assert page.phone_page_summary.get_text() == start_page_phone_summary  # check phone summary

        # Step 3
        page.payment_options_btn.click()

        for i in range(len(page.list_payment_options.get_text())):
            if "6 мес" in page.list_payment_options[i].text:
                save_payment_options = page.list_payment_options[i].text
                page.list_payment_options[i].click()


        page.buy_btn.click()

        assert "https://asmp.a1.by/asmp/LoginMasterServlet" in page.get_current_url()