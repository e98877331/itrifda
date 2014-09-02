import requests

payload = {'ElementName':"something"}
r = requests.post("http://127.0.0.1:8000/fda/getExpertStatement",params=payload)
print r.text
