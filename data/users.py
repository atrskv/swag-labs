import os
import faker
from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    postal_code: str
    login: str
    password: str


fake = faker.Faker()

standart_customer = \
    User(firstname=fake.name_male(),
         lastname=fake.last_name_male(),
         postal_code=fake.postalcode(),
         login=os.getenv('STANDART_CUSTOMER_LOGIN'),
         password=os.getenv('STANDART_CUSTOMER_PASSWORD'))

problem_customer = \
    User(firstname=fake.name_male(),
         lastname=fake.last_name_male(),
         postal_code=fake.postalcode(),
         login=os.getenv('PROBLEM_CUSTOMER_LOGIN'),
         password=os.getenv('PROBLEM_CUSTOMER_PASSWORD'))

locked_out_user = \
    User(firstname=fake.name_male(),
         lastname=fake.last_name_male(),
         postal_code=fake.postalcode(),
         login=os.getenv('LOCKED_OUT_CUSTOMER_LOGIN'),
         password=os.getenv('LOCKED_OUT_CUSTOMER_PASSWORD'))
