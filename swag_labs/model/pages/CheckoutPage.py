from selene.support.shared import browser
from selene import have

from swag_labs.model.controls.text_fields import TextField


class CheckoutPage:

    def open(self):
        browser.open('/checkout-step-one.html')
        return self



    def should_have_exact_text(self, text):
        browser.element('.complete-header').should(have.exact_text(text))
        return self

