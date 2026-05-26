import requests

url = "http://127.0.0.1:8000"


data = {
    "name":"ram",
    "dept":"ece",
    "program":"B.E",
    "DOB":"2005-01-01",
    "batch":"2023-27",
    "email" : "ram@example.com",
    "password":"ram123"
}

#post student
response = requests.post(url+"/add_student", json = data)

print(response.status_code)
print(response.json())

