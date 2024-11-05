import data
import allure

from methods.order_methods import OrderMethods


class TestReceivingOrdersList(OrderMethods):

    @allure.title('Проверяю получение списка заказов по определённому курьеру')
    def test_receiving_orders_list_by_specific_courier(self, login_courier):
        order_params = data.ORDER_PARAMETERS
        order_params['courierId'] = login_courier
        response = self.get_orders_list_method(order_params)
        assert response.ok and response.json()["orders"] == []

    @allure.title('Проверяю получение списка заказов без указания id курьера')
    def test_receiving_orders_list_without_courier_id(self):
        response = self.get_orders_list_method()
        assert response.ok and response.json()["orders"] != []
