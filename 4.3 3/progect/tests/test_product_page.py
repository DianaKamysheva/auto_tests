import pytest
from pages.product_page import ProductPage


class TestProductPage:

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail(reason="Known bug in offer7")
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    def test_guest_can_add_product_to_basket(self, browser, link):
        """
        Тест проверяет добавление товара в корзину для всех промо-акций
        offer7 помечен как xfail из-за известного бага
        """
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Получаем данные товара ДО добавления в корзину
        product_name = page.get_product_name()
        product_price = page.get_product_price()

        # Act - добавляем товар в корзину
        page.add_product_to_basket()

        # Assert - проверяем результаты
        page.should_be_success_message()
        page.should_be_basket_total_message()
        page.should_be_correct_product_name_in_success_message(product_name)
        page.should_be_correct_basket_total(product_price)