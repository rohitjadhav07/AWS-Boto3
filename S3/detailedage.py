import requests
import json
name = input("Enter name: ")
url = "https://api.agify.io/?name=rohit"
try:
    response=requests.get(url)
    data=response.json()
    print(data["age"])

except Exception as e:
    print("Error",e)

with open("agge.json","w") as f:
    json.dump(data,f)