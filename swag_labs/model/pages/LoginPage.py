from selene.support.shared import browser
from selene import have

class LoginPage:

    def open(self):
        browser.open('https://www.saucedemo.com')
        return self



