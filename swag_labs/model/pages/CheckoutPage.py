from selene.support.shared import browser
from selene import have
import allure


class CheckoutPage:

    @allure.step('Открыть страницу "Checkout"')
    def open(self):
        browser.open('/checkout-step-one.html')
        return self

    @allure.step('Заполнить информацию о пользователе')
    def set_users_information(self, firstname='', lastname='', postal_code=''):
        browser.element('#first-name').type(firstname)
        browser.element('#last-name').type(lastname)
        browser.element('#postal-code').type(postal_code)
        return self

    @allure.step('Нажать на кнопку "Continue"')
    def continue_ordering(self):
        browser.element('#continue').click()
        return self

    @allure.step('Нажать на кнопку "Checkout"')
    def go_on(self):
        browser.element('#checkout').click()
        return self

    @allure.step('Нажать на кнопку "Finish"')
    def confirm(self):
        browser.element('#finish').click()
        return self

    @allure.step('Текст "{text}" виден пользователю')
    def successful_order_notification_is_visible(self, text):
        browser.element('.complete-header').should(have.exact_text(text))
        return self

    @allure.step('Текст "{text_message}" отображается на кнопке')
    def error_button_should_have_text(self, text_message):
        browser.element('[data-test=error]').should(have.exact_text(f'Error: {text_message}'))
        return self

