import data
import allure

from methods.base_methods import BaseMethods


class OrderMethods(BaseMethods):

    @allure.step('Отправляю post-запрос на создание нового заказа')
    def post_create_order_method(self, req_body):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_ORDER_CREATE,
            req_data=req_body
        )
        return response

    @allure.step('Отправляю get-запрос на получение списка заказов')
    def get_orders_list_method(self, parameters=''):
        response = self.get_method(
            url=data.BASE_URL,
            req_path=data.PATH_ORDER_CREATE,
            parameters=parameters
        )
        return response
