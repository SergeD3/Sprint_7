import json
import pytest

import data
from helpers import helper
from methods.order_methods import OrderMethods


class TestCreateOrder(OrderMethods):

    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_specific_color(self, color):
        order_body = helper.get_random_order()
        order_body['color'].insert(0, color)
        print(order_body['color'])
        response = self.post_create_order_method(data.ORDER_REQUEST_BODY)
        assert response.ok and response.json()['track']
