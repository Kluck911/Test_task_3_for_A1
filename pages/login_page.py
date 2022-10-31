from pages.base_page import WebPage
from pages.elements import WebElement


class LoginPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://asmp.a1.by/asmp/LoginMasterServlet?service=Portal&cookie=skip&level=10'

        super().__init__(web_driver, url)

    # list smartphone page selectors
    radio_passwrd_btn = WebElement(xpath="//span[2]/label")
    enter_phone_filed = WebElement(css_selector='#itelephone_new')
    enter_password = WebElement(css_selector='#ipassword')
    enter_button = WebElement(xpath='//*[@id="butt1"]/span')
    cart_page_h2 = WebElement(xpath='//h2')
