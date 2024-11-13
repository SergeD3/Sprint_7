import pytest
import allure

from methods.courier_methods import CourierMethods
from helpers import helper


class TestCreateCourier(CourierMethods):

    @allure.title('Проверка создания нового курьера')
    def test_create_courier(self):
        credentials = helper.get_random_courier_credentials()
        response = self.post_create_courier_method(credentials)
        assert response.ok and response.json()["ok"] is True

    @allure.title('Нельзя создать два одинаковых курьера')
    def test_cannot_create_two_identical_couriers(self):
        credentials = helper.get_random_courier_credentials()
        self.post_create_courier_method(credentials)
        second_response = self.post_create_courier_method(credentials)
        assert (second_response.status_code == 409 and
                second_response.json()["message"] == "Этот логин уже используется. Попробуйте другой.")

    @allure.title('Нельзя создать нового курьера с пустыми обязательными полями')
    @pytest.mark.parametrize('credentials', [
        {
            "login": "",
            "password": "1234",
            "firstName": "Курьер Курьерович"
        },
        {
            "login": "courier-3848873",
            "password": "",
            "firstName": "Курьер Курьерович"
        }
    ])
    def test_create_courier_without_required_fields(self, credentials):
        response = self.post_create_courier_method(credentials)
        assert (response.status_code == 400 and
                response.json()["message"] == "Недостаточно данных для создания учетной записи")
