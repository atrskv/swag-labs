from selene.support.shared import browser
import allure


class StartPage:

    @allure.step('Открыть страницу "Start"')
    def open(self):
        browser.open('https://www.saucedemo.com')
        return self

    @allure.step('Войти в аккаунт, используя логин и пароль')
    def log_in(self, login='', password=''):
        browser.element('#user-name').type(login)
        browser.element('#password').type(password)
        browser.element('#login-button').click()
        return self




