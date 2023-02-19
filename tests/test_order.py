from datetime import time

from data.users import standart_customer
from data.products import backpack, jacket, t_shirt
from swag_labs.model.application import Application as app


def test_add_product_to_cart_and_order_it(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .go_to_product_page(backpack.name)
        .add_product_to_cart()
        .go_to_cart()
        .checkout()
        .set_users_information(
            standart_customer.name,
            standart_customer.lastname,
            standart_customer.postal_code)
        .continue_ordering()
        .confirm()

        .successful_order_notification_is_visible()
        )


def test_add_product_to_cart_and_remove_it(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .go_to_product_page(backpack.name)
        .add_product_to_cart()
        .remove_product_from_cart()
        .go_to_cart()

        .cart_should_not_have_a_product()
    )


def test_sort_products_by_price_low_to_high(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .sort_products_by_price_high_to_low()

        .products_should_be_sorted_by_highest_price(
            price=jacket.price)
    )


def test_sort_products_by_name_z_to_a(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .sort_products_by_name_z_to_a()

        .products_should_be_sorted_by_name_z_to_a(
            first_in_sorting=t_shirt.name)
    )


def test_checkout_without_firstname(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .go_to_product_page(jacket.name)
        .add_product_to_cart()
        .go_to_cart()
        .checkout()
        .set_users_information(
            lastname=standart_customer.lastname,
            postal_code=standart_customer.postal_code)
        .continue_ordering()
        .error_button_should_have_text('First Name is required')
        )


def test_checkout_without_lastname(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .go_to_product_page(jacket.name)
        .add_product_to_cart()
        .go_to_cart()
        .checkout()
        .set_users_information(
            name=standart_customer.name,
            postal_code=standart_customer.postal_code)
        .continue_ordering()
        .error_button_should_have_text('Last Name is required')
        )


def test_checkout_without_postal_code(

        given_browser_management,
        given_logged_standart_customer):

    (
        app
        .store_shelf
        .open()
        .go_to_product_page(jacket.name)
        .add_product_to_cart()
        .go_to_cart()
        .checkout()
        .set_users_information(
            name=standart_customer.name,
            lastname=standart_customer.lastname)
        .continue_ordering()
        .error_button_should_have_text('Postal Code is required')
        )


# def test_checkout_without_lastname(browser_management):
#
#
# def test_checkout_without_postal_code(browser_management):
#
#
#
# def continue_shopping_after_adding_the_item_to_cart(browser_management):





