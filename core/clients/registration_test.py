import requests
from pprint import pprint

#{'key': '36ef3125cd47962513d053182e2717f6fb4a16e5'}


def client():
    credentials = {
        'username': 'rest_test_user',
        'email': 'test@test.com',
        'password1': 'testing321..',
        'password2': 'testing321..',
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials,
    )

    print('Status code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
