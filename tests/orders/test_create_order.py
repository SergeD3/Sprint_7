import allure
import pytest

from helpers import helper
from methods.order_methods import OrderMethods


class TestCreateOrder(OrderMethods):

    @allure.title('Проверяю создание заказа с указанием определённого цвета самоката')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_specific_color(self, color):
        order_body = helper.get_random_order()
        order_body['color'].append(color)
        response = self.post_create_order_method(order_body)
        assert response.ok and response.json()['track']
