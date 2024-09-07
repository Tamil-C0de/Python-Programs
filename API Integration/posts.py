import requests
import config

url = config.get_users()

name = input("Enter your name: ")
email = input("Enter your email: ")

data = dict()
data['name'] = name
data['email'] = email
# print(data)

req = requests.post(url, data)
# print(req)