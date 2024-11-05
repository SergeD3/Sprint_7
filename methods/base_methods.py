import json
import requests
import data
import allure


class BaseMethods:

    @staticmethod
    @allure.step('Отправляю get-запрос на указанный эндпоинт')
    def get_method(url, req_path, parameters, body_data=''):
        response = requests.get(
            url=f"{url}{req_path}",
            headers=data.COMMON_HEADERS,
            data=body_data,
            params=parameters
        )
        return response

    @staticmethod
    @allure.step('Отправляю post-запрос на указанный эндпоинт')
    def post_method(url, req_path, req_data='', req_json=''):
        body_data = json.dumps(req_data)
        body_json = json.dumps(req_json)
        response = requests.post(
            url=f"{url}{req_path}",
            headers=data.COMMON_HEADERS,
            data=body_data,
            json=body_json
        )
        return response
