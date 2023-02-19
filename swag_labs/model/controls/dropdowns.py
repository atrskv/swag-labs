from selene.support.shared import browser

from selene import Element

class Dropdown:

    def __init__(self, element: Element):
        self.element = element

    def sort_by(self, value='az'):
        browser.element(f'[value={value}]').click()



