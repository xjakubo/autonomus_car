import requests
from time import time
from requestarguments import Request_Arguments
import random

json = {
    "speed": 90,
    "forward": True
    }

url = "http://192.168.4.1/"
arguments = Request_Arguments()
times = []
print("starting test")
session = requests.Session()
while len(times) < 100:
    start = time()
    #arguments.changeSpeed(random.randint(1,100), True)
    req = session.post(url, json=arguments.getRequestArguments(), timeout = 5)
    times.append(time() - start)
    #print(req.text)

print(sum(times)/len(times))
