from selene.support.shared import browser
from selene import have, be

from swag_labs.model.controls.buttons import Button
from swag_labs.model.controls.dropdowns import Dropdown
from swag_labs.model.controls.text_fields import TextField


class StoreShelfPage:

    def open(self):
        browser.open('/inventory.html')
        return self

    def go_to_product_page(self, product_name: str):
        browser.all('.inventory_item_name').element_by(have.exact_text(product_name)).click()
        return self

    def add_product_to_cart(self):
        browser.element('[name^=add-to-cart]').click()
        return self

    def go_to_cart(self):
        browser.element('.shopping_cart_link').click()
        return self

    def set_users_information(self, firstname='', lastname='', postal_code=''):
        browser.element('#first-name').type(firstname)
        browser.element('#last-name').type(lastname)
        browser.element('#postal-code').type(postal_code)
        return self



    def checkout(self):
        browser.element('#checkout').click()
        return self

    def continue_ordering(self):
        browser.element('#continue').click()
        return self

    def confirm(self):
        browser.element('#finish').click()
        return self

    def remove_product_from_cart(self):
        browser.element('.btn_small').click()
        return self


    def successful_order_notification_is_visible(self):
        browser.element('.complete-header').should(have.exact_text('THANK YOU FOR YOUR ORDER'))
        return self


    def error_button_should_have_text(self, text_message):
        browser.element('[data-test=error]').should(have.exact_text(f'Error: {text_message}'))
        return self


    def cart_should_not_have_a_product(self):
        browser.element('.cart_item').should(be._not_.visible)
        return self


    def sort_products_by_name_a_to_z(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='az')
        return self

    def sort_products_by_name_z_to_a(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='za')
        return self

    def sort_products_by_price_low_to_high(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='lohi')
        return self

    def sort_products_by_price_high_to_low(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='hilo')
        return self

    def products_should_be_sorted_by_highest_price(self, price):
        browser.all('.inventory_item_price').first.should(have.exact_text(f'${price}'))
        return self

    def products_should_be_sorted_by_name_z_to_a(self, first_product_in_sorting):
        browser.all('.inventory_item_name').first.should(have.text(first_product_in_sorting))
        return self


    def back_to_products(self):
        browser.element('#back-to-products').click()
        return self









