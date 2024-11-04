import data
import pytest

from helpers import helper
from methods.courier_methods import CourierMethods


class TestCourierAuthorization(CourierMethods):

    def test_existing_courier_auth(self):
        response = self.post_login_courier_method(data.COURIER_CREDENTIALS)
        assert response.ok and response.json()["id"] == 416280

    @pytest.mark.parametrize('credentials', (
            {"login": "ninja8849", "password": ""},
            {"login": "", "password": "1234"}
    ))
    def test_courier_auth_without_required_fields(self, credentials):
        response = self.post_login_courier_method(credentials)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    def test_not_existing_courier_auth(self):
        credentials = helper.get_random_courier_credentials()
        response = self.post_login_courier_method(credentials)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize('credentials', (
            {"login": "wrong_ninja8849", "password": "1234"},
            {"login": "ninja8849", "password": "wrong_1234"}
    ))
    def test_courier_auth_bad_credentials(self, credentials):
        response = self.post_login_courier_method(credentials)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
