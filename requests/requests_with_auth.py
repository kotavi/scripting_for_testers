import requests

url = "http://api.github.com/user"
response = requests.get(url)
print(response.json())
print(response.status_code)


# response = requests.get(url, auth=('username', 'password'))
# print(response.json()['message'])
# print(response.status_code)
# assert response.json()['message'] == 'Must specify two-factor authentication OTP code.'

response = requests.get(url, headers={'Authorization': 'Bearer <personal access tokens>'})
print(response.json())
print(response.status_code)
assert response.json()['login']

for key in response.json().keys():
    print(key)
