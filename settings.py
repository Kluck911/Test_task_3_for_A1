class User:
    def __init__(self, phone, password):
        self.login = phone
        self.passwrd = password


test_user = User(phone="111111111", password="aaaaaa")
valid_user = User(phone="259397578", password="klicKKluck_1812")