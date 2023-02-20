import allure
from swag_labs.model.application import Application as app


@allure.tag('web')
@allure.title('Добавление товаров в корзину и оформление заказа')
def test_add_product_to_cart_and_order_it(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['backpack'].name)
        .add_product_to_cart()
        .go_to_cart())
    (
        app
    .checkout
        .go_on()
        .set_users_information(
            standart_customer.firstname,
            standart_customer.lastname,
            standart_customer.postal_code)
        .continue_ordering()
        .confirm()


        .successful_order_notification_is_visible('THANK YOU FOR YOUR ORDER')
    )


@allure.tag('web')
@allure.title('Добавление товаров в корзину и её удаление из корзины')
def test_add_product_to_cart_and_remove_it(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['backpack'].name)
        .add_product_to_cart()
        .remove_product_from_cart()
        .go_to_cart()


        .cart_should_not_have_a_product()
    )

@allure.tag('web')
@allure.title('Сортировка товаров по цене от большего к меньшему')
def test_sort_products_by_price_high_to_low(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .sort_products_by_price_high_to_low()


        .products_should_be_sorted_by_highest_price(
            highest_price=products['jacket'].price)
    )

@allure.tag('web')
@allure.title('Сортировка товаров по имени от "Z" до "A"')
def test_sort_products_by_name_z_to_a(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .sort_products_by_name_z_to_a()


        .products_should_be_sorted_by_name_z_to_a(
            first_product_in_sorting=products['t_shirt'].name)
    )

@allure.tag('web')
@allure.title('Оформление заказа без указания имени')
def test_checkout_without_firstname(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['jacket'].name)
        .add_product_to_cart()
        .go_to_cart())
    (
        app
    .checkout
        .go_on()
        .set_users_information(
            lastname=standart_customer.lastname,
            postal_code=standart_customer.postal_code)
        .continue_ordering()


        .error_button_should_have_text('First Name is required')
        )

@allure.tag('web')
@allure.title('Оформление заказа без указания фамилии')
def test_checkout_without_lastname(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['jacket'].name)
        .add_product_to_cart()
        .go_to_cart())
    (
        app
    .checkout
        .go_on()
        .set_users_information(
            firstname=standart_customer.firstname,
            postal_code=standart_customer.postal_code)
        .continue_ordering()


        .error_button_should_have_text('Last Name is required')
        )

@allure.tag('web')
@allure.title('Оформление заказа без почтового кода')
def test_checkout_without_postal_code(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['jacket'].name)
        .add_product_to_cart()
        .go_to_cart())
    (
        app
    .checkout
        .go_on()
        .set_users_information(
            firstname=standart_customer.firstname,
            lastname=standart_customer.lastname)
        .continue_ordering()


        .error_button_should_have_text('Postal Code is required')
    )

@allure.tag('web')
@allure.title('Возврат к просмотру товаров после добавления вещи в корзину и оформление заказа')
def test_continue_shopping_after_adding_the_item_to_cart(


        browser_management,
        standart_customer,
        products):


    (
        app
    .store_shelf
        .open()
        .go_to_product_page(products['backpack'].name)
        .add_product_to_cart()
        .back_to_products()
        .go_to_product_page(products['jacket'].name)
        .add_product_to_cart()
        .go_to_cart())
    (
        app
    .checkout
        .go_on()
        .set_users_information(
            standart_customer.firstname,
            standart_customer.lastname,
            standart_customer.postal_code)
        .continue_ordering()
        .confirm()


        .successful_order_notification_is_visible('THANK YOU FOR YOUR ORDER')
    )





