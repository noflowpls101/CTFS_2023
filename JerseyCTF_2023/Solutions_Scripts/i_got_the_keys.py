import requests

headers = {
    'authorization_key': 'GdERHpBh3x'
}

r = requests.get("http://localhost:3000/flag", headers=headers)
print(r.text)
