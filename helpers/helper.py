import json
import random
import string
import data
import copy


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def get_random_courier_credentials():
    creds_copy = copy.deepcopy(data.COURIER_CREDENTIALS)

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    creds_copy['login'] = login
    creds_copy['password'] = password
    creds_copy['firstName'] = first_name

    return creds_copy


def get_random_order():
    order_copy = copy.deepcopy(data.ORDER_REQUEST_BODY)

    first_name = generate_random_string(10)
    last_name = generate_random_string(10)
    station_number = random.randint(1, 10)

    order_copy['firstName'] = first_name
    order_copy['lastName'] = last_name
    order_copy['metroStation'] = station_number
    return order_copy


if __name__ == '__main__':
    print(get_random_courier_credentials())
