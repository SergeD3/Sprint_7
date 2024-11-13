import json

import pytest
import requests

import data
from helpers import helper


@pytest.fixture
def login_courier():
    def login(credentials=None):
        req_data = json.dumps(credentials) if credentials else json.dumps(data.COURIER_CREDENTIALS)
        response = requests.post(
            url=f"{data.BASE_URL}{data.PATH_COURIER_LOGIN}",
            headers=data.COMMON_HEADERS,
            data=req_data
        )

        if response.ok:
            return response.json()['id']
        else:
            print(f"Ошибка попытки аутентификации.")

    return login


@pytest.fixture
def create_courier(login_courier):
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
    payload_json = json.dumps(payload)
    response = requests.post(f"{data.BASE_URL}{data.PATH_COURIER_CREATE}",
                             data=payload_json,
                             headers=data.COMMON_HEADERS
                             )

    if response.ok:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    courier_id = login_courier(payload)
    requests.delete(url=f"{data.BASE_URL}{data.PATH_COURIER_CREATE}{courier_id}")
