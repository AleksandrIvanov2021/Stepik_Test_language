import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(5)  # для визуальной проверки языка открытой страницы
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")  # Проверяем наличие кнопки

    # Пример для запуска в командной строке: pytest -s -v --language=es test_items.py
    #                                        pytest -s -v --language=fr test_items.py
