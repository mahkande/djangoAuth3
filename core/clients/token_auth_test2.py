import requests
from pprint import pprint

#{'key': '1b688dff4cca4a76d127efcde2077faaf48a725c'}


def client():
    token = 'Token 36ef3125cd47962513d053182e2717f6fb4a16e5'
    headers = {
        'Authorization': token,
    }
    response = requests.get(
        url='http://localhost:8000/api/kullanici-profilleri/',
        headers=headers,
    )

    print('Status code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
