# import requests

# req = requests.get('https://jsonplaceholder.typicode.com/users')
# # print(req.json())
# print(type(req.text))

import requests
import config

url = config.get_users()
# id = input("Enter user id: ")

# url = url + id
# print(url)
req = requests.get(url)
print(req.json())