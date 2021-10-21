import requests
from pprint import pprint

#{'key': '1b688dff4cca4a76d127efcde2077faaf48a725c'}


def client():
    credentials = {
        'username': 'ck',
        'password': 'testing321..'
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
    )

    print('Status code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
