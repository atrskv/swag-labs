from selene.support.shared import browser
from selene import have, be
from swag_labs.model.controls.dropdowns import Dropdown
import allure


class StoreShelfPage:

    @allure.step('Открыть страницу "Products"')
    def open(self):
        browser.open('/inventory.html')
        return self

    @allure.step('Перейти на страницу товара "{product_name}"')
    def go_to_product_page(self, product_name: str):
        browser.all('.inventory_item_name').element_by(have.exact_text(product_name)).click()
        return self

    @allure.step('Добавить товар в корзину')
    def add_product_to_cart(self):
        browser.element('[name^=add-to-cart]').click()
        return self

    @allure.step('Перейти в корзину')
    def go_to_cart(self):
        browser.element('.shopping_cart_link').click()
        return self

    @allure.step('Удалить товар из корзины')
    def remove_product_from_cart(self):
        browser.element('.btn_small').click()
        return self

    @allure.step('В корзине не отображается выбранный товар')
    def cart_should_not_have_a_product(self):
        browser.element('.cart_item').should(be._not_.visible)
        return self

    @allure.step('Отсортировать товары по имени от "Z" до "A"')
    def sort_products_by_name_z_to_a(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='za')
        return self

    @allure.step('Отсортировать товары по цене от большего к меньшему')
    def sort_products_by_price_high_to_low(self):
        Dropdown(browser.element('.product_sort_container')).sort_by(value='hilo')
        return self

    @allure.step('Товары отсортированы по цене от большего к меньшему')
    def products_should_be_sorted_by_highest_price(self, highest_price):
        browser.all('.inventory_item_price').first.should(have.exact_text(f'${highest_price}'))
        return self

    @allure.step('Товары отсортированы по имени от "Z" до "A"')
    def products_should_be_sorted_by_name_z_to_a(self, first_product_in_sorting):
        browser.all('.inventory_item_name').first.should(have.text(first_product_in_sorting))
        return self

    @allure.step('Вернуться на страницу просмотра товаров')
    def back_to_products(self):
        browser.element('#back-to-products').click()
        return self









