import requests

url = "http://127.0.0.1:8000"


#delete student
id = int(input("ID: ")) 
response = requests.delete(url+f"/delete/{id}")

print(response.status_code)
print(response.json())

