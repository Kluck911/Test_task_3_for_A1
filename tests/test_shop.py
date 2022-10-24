import random

from pages.shop_page import ShopPages
from settings import test_user, valid_user


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
        assert page.smart_page_h1.get_text() == start_page_phone_summary  # check phone summary

        # Step 3
        page.payment_options_btn.click()
        save_payment_options = ''
        for i in range(len(page.list_payment_options.get_text())):
            if "6 мес" in page.list_payment_options[i].text:
                save_payment_options = page.list_payment_options[i].text
                page.list_payment_options[i].click()

        assert page.pay_in_mounth.get_text() in save_payment_options

        # Step 4
        page.buy_btn.click()

        assert "https://asmp.a1.by/asmp/LoginMasterServlet" in page.get_current_url()
        assert page.smart_page_h1.get_text() == "Вход в аккаунт"

        # Step 5
        page.radio_passwrd_btn.click()
        page.enter_phone_filed.send_keys(valid_user.login)
        page.enter_password.send_keys(valid_user.passwrd)
        page.enter_button.click()

        assert "Выбор размера и срока платежа" in page.cart_page_h2.get_text()

        # Step 6

        phone_cart_summary = page.cart_phone_summary.get_text()
        phone_mounths_pay = page.cart_phone_descr[0].text
        phone_pay_value = page.cart_phone_descr[1].text
        print(f"\nВыбран {phone_cart_summary}, вариант оплаты: {phone_mounths_pay} {phone_pay_value}")

        assert phone_cart_summary == start_page_phone_summary  # название тел. в корзине совпадает с  выбранным на
                                                                # начальной странице

        # Выберите True чтобы включить проверку совпадения способа оплаты в корзине и на странице телефона
        last_check = False

        if last_check:
            assert phone_pay_value in save_payment_options  # проверяем что  выбранный в корзине способ оплаты совпадает
                                                            # со способом выбранном на странице телефона
