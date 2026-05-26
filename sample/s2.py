import requests

url = "http://127.0.0.1:8000"


#get student by id
id = int(input("Enter id: "))
response = requests.get(url+f"/student/{id}")

print(response.status_code)
print(response.json())

