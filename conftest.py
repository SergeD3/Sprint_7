import pytest
import requests
from helpers import helper


@pytest.fixture
def courier():
    login_pass = []
    login = helper.generate_random_string(10)
    password = helper.generate_random_string(10)
    first_name = helper.generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == response.ok:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass
