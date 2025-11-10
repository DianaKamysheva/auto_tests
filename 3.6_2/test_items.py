import time


def test_add_to_cart_button_presence(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Задержка для визуальной проверки языка
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")

    # Утверждение, что кнопка найдена
    assert len(add_to_cart_button) > 0, "Add to cart button is not found on the page"

    # Дополнительная проверка, что кнопка видима
    assert add_to_cart_button[0].is_displayed(), "Add to cart button is not visible"