from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name_product.text

    def should_be_alert_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET), "Alert is not present"
        alert_name_product = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET)[0]
        assert alert_name_product.text == self.get_name_product(), "Product name is not expected name"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_product_price_in_alert_is_product_price(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET), "Alert is not present"
        price_product_in_alert = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET)[2]
        assert price_product_in_alert.text == self.get_product_price(), "Product price in alert is not product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but didn't"
