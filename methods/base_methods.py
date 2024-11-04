import json

import requests

import data


class BaseMethods:

    def get_method(self):
        pass

    @staticmethod
    def post_method(url, req_path, req_body=None, req_json=None):
        if req_body:
            body_json = json.dumps(req_body)
            response = requests.post(
                url=f"{url}{req_path}",
                headers=data.COMMON_HEADERS,
                data=body_json
            )
            return response
        elif req_json:
            body_json = json.dumps(req_json)
            response = requests.post(
                url=f"{url}{req_path}",
                headers=data.COMMON_HEADERS,
                json=body_json
            )
            return response
        else:
            print('Необходимо указать data или json для запроса.')

    def put_method(self):
        pass

    def delete_method(self):
        pass
