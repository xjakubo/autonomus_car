import requests
from time import time
from requestarguments import Request_Arguments
import random


url = "http://192.168.4.1/"
arguments = Request_Arguments()
times = []
print("starting test")
session = requests.Session()
while len(times) < 30:
    start = time()
    arguments.changeSpeed(random.randint(1,100), random.choice([True,False]))
    arguments.changeDir(random.randint(-100,100))
    req = session.post(url, json=arguments.getRequestArguments(), timeout = 5)
    times.append(time() - start)
    print(f"{len(times)} request OK")
    print(arguments.getRequestArguments())
    #print(req.text)

arguments.changeSpeed(0, True)
arguments.changeDir(0)
session.post(url, json = arguments.getRequestArguments(), timeout = 5)
print(sum(times)/len(times))
