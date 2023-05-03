import requests
import re

r = requests.get("http://localhost:3001/")
print(r.cookies)

