import requests
import json
res = requests.get('http://localhost:8000')
print(res.text)

res = requests.get('http://localhost:8000/students_filtered?minsal=1000&maxsal=1200')
print(res.text)


url = "http://localhost:8000/employees"
headers = {
                'content-type': "application/json"
        }
response = requests.request("POST", url, headers=headers,json={"eid":"E005", "ename": "Dan","sal":1400})
print(response.text)

url ="http://localhost:8000/employees/E001"
headers = {
                'content-type': "application/json"
        }
response = requests.request("PUT", url, headers=headers,json={"eid":"E001", "ename": "Ran","sal":1500})
print(response.text)


url ="http://127.0.0.1:8000/employees/E002"
headers = {
                'content-type': "application/json"
        }
response = requests.request("DELETE", url)
print(response.text)
