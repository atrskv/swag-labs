import os
from dataclasses import dataclass

from dotenv import load_dotenv
from selene.support.shared import browser
from selene import be, have
load_dotenv()

from swag_labs.model.controls.text_fields import TextField
from swag_labs.model.controls.buttons import Button



from swag_labs.model.pages.LoginPage import LoginPage

from swag_labs.model.application import Application as app




def test_add_product_to_cart_and_checkout(browser_management):

    @dataclass
    class Product:
        name: str
        description: str
        price: str

    backpack = Product(name='Sauce Labs Backpack',
                    description='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.',
                    price='29.99')


    login = os.getenv('STANDART_USER_LOGIN')
    password = os.getenv('STANDART_USER_PASSWORD')

    app.login.open()

    TextField(browser.element('#user-name')).type_login(login)

    TextField(browser.element('#password')).type_password(password)

    Button(browser.element('#login-button')).click_login_button()

    app.inventory.should_have_items(6)


    browser.all('.inventory_item_name').element_by(have.exact_text(backpack.name)).click()

    browser.element('[data-test^=add-to-cart]').click()

    browser.element('.shopping_cart_link').click()


    browser.element('#checkout').click()

    browser.element('#first-name').type('Name')
    browser.element('#last-name').type('Lastname')
    browser.element('#postal-code').type('123123')

    browser.element('#continue').click()

    browser.element('#finish').click()

    browser.element('.complete-header').should(have.exact_text('THANK YOU FOR YOUR ORDER'))

    # def test_add_product_to_cart_and_remove(browser_management):
    #
    #
    #
    #
    # def test_checkout_without_firstname(browser_management):
    #
    #
    #
    # def test_checkout_without_lastname(browser_management):
    #
    #
    # def test_checkout_without_postal_code(browser_management):
    #
    #
    #
    # def continue_shopping_after_adding_the_item_to_cart(browser_management):
    #
    #
    #


