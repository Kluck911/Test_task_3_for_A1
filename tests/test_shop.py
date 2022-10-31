import json
import random

from pages.shop_page import ShopPages
from pages.smart_page import SmartphonePage
from pages.loginPage import LoginPage
from pages.cart_page import CartPage
from settings import valid_user

start_page_phone_summary = None
save_payment_options = None


class TestsA1Shop:

    def test_step_1(self, web_browser):

        page = ShopPages(web_browser)

        web_browser.execute_script("window.localStorage.setItem('{}',{})".format('cookieAccepted', json.dumps('true')))
        web_browser.refresh()  # Send cookieAccepted is true in localStorage and refresh page

        assert page.get_current_url() == 'https://www.a1.by/ru/c/shop', 'shop page url error'

    def test_step_2(self, web_browser):
        page = ShopPages(web_browser)
        rnd_number = random.randint(0, len(page.list_stock_phone_btn.get_text()) - 1)  # random number for phone block

        global start_page_phone_summary
        start_page_phone_summary = page.list_phone_summary.get_text()[rnd_number]  # save smartphone summary
        page.list_stock_phone_btn[rnd_number].click()

        assert 'https://www.a1.by/ru/shop/phones/smartphones' in page.get_current_url()  # check url

        assert page.smart_page_h1.get_text() == start_page_phone_summary  # check phone summary

    def test_step_3(self, web_browser):
        page = SmartphonePage(web_browser, url=web_browser.current_url)
        page.payment_options_btn.click()
        global save_payment_options
        for i in range(len(page.list_payment_options.get_text())):
            if "6 мес" in page.list_payment_options[i].text:
                save_payment_options = page.list_payment_options[i].text
                page.list_payment_options[i].click()

        assert page.pay_in_mounth.get_text() in save_payment_options

    def test_step_4(self, web_browser):
        page = SmartphonePage(web_browser, url=web_browser.current_url)
        page.buy_btn.click()

        assert "https://asmp.a1.by/asmp/LoginMasterServlet" in page.get_current_url()
        assert page.smart_page_h1.get_text() == "Вход в аккаунт"

    def test_step_5(self, web_browser):
        page = LoginPage(web_browser, url=web_browser.current_url)
        page.radio_passwrd_btn.click()
        page.enter_phone_filed.send_keys(valid_user.login)
        page.enter_password.send_keys(valid_user.passwrd)
        page.enter_button.click()

        assert "Выбор размера и срока платежа" in page.cart_page_h2.get_text()

    def test_step_6(self, web_browser):
        page = CartPage(web_browser, url=web_browser.current_url)
        phone_cart_summary = page.cart_phone_summary.get_text()
        phone_months_pay = page.cart_phone_descr[0].text
        phone_pay_value = page.cart_phone_descr[1].text
        print(f"\nВыбран {phone_cart_summary}, вариант оплаты: {phone_months_pay} {phone_pay_value}")

        assert phone_cart_summary == start_page_phone_summary  # Название тел. в корзине совпадает с выбранным на
        # начальной странице

        # Выберите True, чтобы включить проверку совпадения способа оплаты в корзине и на странице телефона
        last_check = False

        if last_check:
            assert phone_pay_value in save_payment_options  # проверяем что выбранный в корзине способ оплаты совпадает
            # со способом выбранном на странице телефона
