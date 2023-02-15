from selene import Element

class TextField:

    def __init__(self, element: Element):
        self.element = element

    def type_login(self, login: str):
        self.element.type(login)

    def type_password(self, password: str):
        self.element.type(password)

    def type_name(self, name: str):
        self.element.type(name)

    def type_lastname(self, lastname: str):
        self.element.type(lastname)