from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    # Локаторы
    ADD_TO_BASKET_BUTTON = ("css selector", "button.btn-add-to-basket")
    PRODUCT_NAME = ("css selector", "div.product_main h1")
    PRODUCT_PRICE = ("css selector", "p.price_color")
    SUCCESS_MESSAGE = ("css selector", "div.alert-success .alertinner strong")
    BASKET_TOTAL_MESSAGE = ("css selector", "div.alert-info .alertinner strong")

    def add_product_to_basket(self):
        """Добавляет товар в корзину и решает quiz"""
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        """Возвращает название товара со страницы"""
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара со страницы"""
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message(self):
        """Проверяет, что есть сообщение об успешном добавлении"""
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_basket_total_message(self):
        """Проверяет, что есть сообщение со стоимостью корзины"""
        assert self.is_element_present(*self.BASKET_TOTAL_MESSAGE), "Basket total message is not presented"

    def should_be_correct_product_name_in_success_message(self, expected_product_name):
        """Проверяет, что название товара в сообщении совпадает с ожидаемым"""
        actual_product_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert expected_product_name == actual_product_name, \
            f"Product name in message doesn't match. Expected: '{expected_product_name}', got: '{actual_product_name}'"

    def should_be_correct_basket_total(self, expected_price):
        """Проверяет, что стоимость корзины совпадает с ценой товара"""
        actual_basket_total = self.browser.find_element(*self.BASKET_TOTAL_MESSAGE).text
        assert expected_price == actual_basket_total, \
            f"Basket total doesn't match product price. Expected: '{expected_price}', got: '{actual_basket_total}'"

    def add_to_basket_with_checks(self):
        """Полный сценарий добавления в корзину с проверками"""
        # Получаем данные товара ДО добавления в корзину
        product_name = self.get_product_name()
        product_price = self.get_product_price()

        # Добавляем товар в корзину
        self.add_product_to_basket()

        # Проверяем сообщения
        self.should_be_success_message()
        self.should_be_basket_total_message()
        self.should_be_correct_product_name_in_success_message(product_name)
        self.should_be_correct_basket_total(product_price)