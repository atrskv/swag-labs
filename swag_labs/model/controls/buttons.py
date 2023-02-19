from selene import Element

class Button:

    def __init__(self, element: Element):
        self.element = element

    def click_login_button(self):
        self.element.click()




    def go_to_cart(self):
        self.element.click()

    def checkout(self):
        self.element.click()

    def continue_ordering_proccess(self):
        self.element.click()

    def confirm(self):
        self.element.click()

