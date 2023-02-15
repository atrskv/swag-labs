from selene import Element

class Button:

    def __init__(self, element: Element):
        self.element = element

    def click_login_button(self):
        self.element.click()