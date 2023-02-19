from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    price: str


backpack = \
    Product(name='Sauce Labs Backpack',
            description='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.',
            price='29.99')


jacket = \
    Product(name='Sauce Labs Fleece Jacket',
            description='It\'s not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.',
            price='49.99')


t_shirt = \
    Product(name='Test.allTheThings() T-Shirt (Red)',
            description='This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.',
            price='15.99')





