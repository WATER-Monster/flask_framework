import threading
import requests

def send(num):
    res = requests.get("http://localhost:8000/api/test?name=%s" % num)
    print(num, res.text)

for i in range(40):
    t = threading.Thread(target=send, args=(i,))
    t.start()