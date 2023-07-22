import configuration
import requests


def post_create_order(headers, order_data):
    response = requests.post(
        configuration.domain + configuration.path_create_order,
        json=order_data,
        headers=headers
    )
    if (response.status_code == 201):
        return str(response.json()["track"])
    else:
        print("Не могу создать пользователя! Ошибка: " +
              str(response.status_code))
        exit(1)


def get_get_order(track_number):
    response = requests.get(
        configuration.domain + configuration.path_get_order + "?t=" + track_number
    )
    return response.status_code
