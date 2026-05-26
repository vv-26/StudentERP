import requests

url = "http://127.0.0.1:8000"


#update student
id = int(input("ID: "))
dept = input("New Dept: ")
program = input("New program: ")
password = input("password: ")
data = {"dept":dept, "program":program,"password":password}

response = requests.put(url+f"/update/{id}", json=data)

print(response.status_code)
print(response.json())

