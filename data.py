COURIER_CREDENTIALS = {
    "login": "ninja8849",
    "password": "1234",
    "firstName": ""
}

ORDER_REQUEST_BODY = {
    "firstName": "",
    "lastName": "",
    "address": "tower, 142 apt.",
    "metroStation": "",
    "phone": "+7 949 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-11-10",
    "comment": "lala lala la",
    "color": []
}

COMMON_HEADERS = {'Content-Type': 'application/json'}
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'

PATH_COURIER_LOGIN = '/courier/login'
PATH_COURIER_CREATE = '/courier'

PATH_ORDER_CREATE = '/api/v1/orders'