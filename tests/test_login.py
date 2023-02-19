from swag_labs.model.application import Application as app
from data.users import standart_customer, locked_out_user


def test_login(

        given_browser_management):

    (
        app
        .start
        .open()
        .log_in(
            standart_customer.login,
            standart_customer.password
        )

        .store_shelf_have_items()
    )

def test_locked_out_user_login(

        given_browser_management):

    (
        app
        .start
        .open()
        .log_in(login=locked_out_user.login,
                password=locked_out_user.password)

        .error_button_should_have_text('Sorry, this user has been locked out.')
    )


def test_log_in_without_login(

        given_browser_management):

    (
        app
        .start
        .open()
        .log_in(password=standart_customer.password)

        .error_button_should_have_text('Username is required')
    )

def test_login_without_password(

        given_browser_management):

    (
        app
        .start
        .open()
        .log_in(login=standart_customer.login)

        .error_button_should_have_text('Password is required')
    )


