import os
from dataclasses import dataclass

import faker

fake = faker.Faker()

@dataclass
class User:
    firstname: str
    lastname: str
    postal_code: str
    login: str
    password: str




standart_customer = \
    User(firstname=fake.name_male(),
         lastname=fake.last_name_male(),
         postal_code=fake.postalcode(),
        login=os.getenv('STANDART_CUSTOMER_LOGIN'),
        password=os.getenv('STANDART_CUSTOMER_PASSWORD')
    )

