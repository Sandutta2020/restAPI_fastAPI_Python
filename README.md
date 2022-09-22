uvicorn app:app --reload

curl http://127.0.0.1:8000/students


curl "http://127.0.0.1:8000/students?mini=16&maxi=18"


curl http://127.0.0.1:8000/students/0
