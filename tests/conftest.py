import os

import faker as faker
import pytest
from selene.support.shared import browser
from dotenv import load_dotenv

from data.products import Product
from data.users import standart_customer, User
from swag_labs.model.application import Application as app
import faker

fake = faker.Faker()

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('BASE_URL')
    browser.config.hold_browser_open = False


    yield


    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def standart_customer():

    standart_customer = \
        User(firstname=fake.name_male(),
             lastname=fake.last_name_male(),
             postal_code=fake.postalcode(),
             login=os.getenv('STANDART_CUSTOMER_LOGIN'),
             password=os.getenv('STANDART_CUSTOMER_PASSWORD'))

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

    return standart_customer


@pytest.fixture(scope='function', autouse=False)
def products():

    backpack = Product(name='Sauce Labs Backpack',
                description='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.',
                price='29.99')

    jacket = Product(name='Sauce Labs Fleece Jacket',
                description='It\'s not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.',
                price='49.99')

    t_shirt = Product(name='Test.allTheThings() T-Shirt (Red)',
                description='This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.',
                price='15.99')

    products = {'backpack': backpack, 'jacket': jacket, 't_shirt': t_shirt}

    return products



