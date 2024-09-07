import requests
import config

url = config.get_users()
id = input("Enter an id to delete: ")
url += id

req = requests.delete(url)
print(req)