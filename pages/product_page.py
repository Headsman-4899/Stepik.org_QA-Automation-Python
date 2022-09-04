from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name_product.text

    def should_be_alert_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET), "Alert is not present"
        alert_name_product = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_BASKET)[0]
        assert alert_name_product.text == self.get_product_name(), "Product name is not expected name"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def add_item_to_basket(self):
        add_item_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_item_button.click()

    def should_be_equal_names_and_prices(self, item_name, item_price):
        self.should_be_same_book_name(item_name)
        self.should_be_same_price(item_price)

    def should_be_same_book_name(self, item_name):
        book_name = item_name
        assert self.is_element_present(*ProductPageLocators.ADDING_INFO), 'Success message is not presented'
        info_book_name = self.browser.find_element(*ProductPageLocators.ADDING_INFO).text
        assert book_name == info_book_name, 'Books names are not the same'

    def should_be_same_price(self, item_price):
        book_price = item_price
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE_INFO), 'Basket value message is not presented'
        info_basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_INFO).text
        assert book_price == info_basket_value, 'Prices are not the same'

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
