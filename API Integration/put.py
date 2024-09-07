import requests
import config

url = config.get_users()
id = input("Enter user id to update: ")
email = input("Enter a updated email: ")

url = url + id

updated_data = {
    "name": "Breitenberg",
    "email": email,
    "id": id 
}

req = requests.put(url, data=updated_data)
print(req)