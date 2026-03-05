import requests
import json
name = input("Enter name: ")
url = f"https://api.nationalize.io/?name={name}"
response=requests.get(url)
print(response.json())