import pytest
from selene.support.shared import browser
from dotenv import load_dotenv
from data.users import standart_customer
from swag_labs.model.application import Application as app

@pytest.fixture(scope='function', autouse=True)
def given_browser_management():
    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.hold_browser_open = False


    yield


    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def given_standart_customer():

    load_dotenv()

    (
        app
        .start
        .open()
        .log_in(
            standart_customer.login,
            standart_customer.password
        )

    )