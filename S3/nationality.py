import requests
import json
name = input("Enter name: ")
url = "https://api.nationalize.io/?name=rohit"

    response=requests.get(url)
    print(response.json())
