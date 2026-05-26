import requests

url = "http://127.0.0.1:8000"


#all students
response = requests.get(url+"/all_students")

print(response.status_code)
print(response.json())

