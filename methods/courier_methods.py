import data
import allure

from methods.base_methods import BaseMethods


class CourierMethods(BaseMethods):

    @allure.step('Отправляю post-запрос на создание курьера')
    def post_create_courier_method(self, credentials):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_COURIER_CREATE,
            req_data=credentials
        )
        return response

    @allure.step('Отправляю post-запрос для аутентификации курьера')
    def post_login_courier_method(self, credentials):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_COURIER_LOGIN,
            req_data=credentials
        )
        return response
