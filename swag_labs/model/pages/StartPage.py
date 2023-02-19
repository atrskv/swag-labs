from selene.support.shared import browser
from selene import have
from swag_labs.model.controls.buttons import Button

class StartPage:

    def open(self):
        browser.open('https://www.saucedemo.com')
        return self

    def log_in(self, login='', password=''):
        browser.element('#user-name').type(login)
        browser.element('#password').type(password)
        browser.element('#login-button').click()
        return self

    def store_shelf_have_items(self, amount=6):
        browser.element('.inventory_list').all('.inventory_item').should(have.size(amount))
        return self


    def error_button_should_have_text(self, text_message):
        browser.element('[data-test=error]').should(have.exact_text(f'Epic sadface: {text_message}'))
        return self




