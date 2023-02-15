from selene.support.shared import browser
from selene import have

class InventoryPage:

    def open(self):
        browser.open('/inventory.html')
        return self


    def should_have_items(self, amount):
        browser.element('.inventory_list').all('.inventory_item').should(have.size(amount))
