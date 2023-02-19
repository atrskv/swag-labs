import os
from dataclasses import dataclass

import faker

fake = faker.Faker()

@dataclass
class User:
    name: str
    lastname: str
    postal_code: str
    login: str
    password: str




standart_customer = \
    User(name='Aleksei',
         lastname='Torsukov',
         postal_code='20018',
        login=os.getenv('STANDART_CUSTOMER_LOGIN'),
        password=os.getenv('STANDART_CUSTOMER_PASSWORD')
    )

