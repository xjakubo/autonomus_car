import requests
from time import time, sleep
from requestarguments import Request_Arguments
import random


url = "http://192.168.4.1/"
arguments = Request_Arguments()
times = []
print("starting test")
for i in range(3):
    print(f'STARTING IN {3-i}')
    sleep(1)
session = requests.Session()
start = time()
arguments.changeSpeed(99 , True)
arguments.changeDir(99)
req = session.post(url, json=arguments.getRequestArguments(), timeout = 5)
times.append(time() - start)
print(arguments.getRequestArguments())
#print(req.text)
sleep(1)
arguments.changeSpeed(0, True)
arguments.changeDir(0)
session.post(url, json = arguments.getRequestArguments(), timeout = 5)
print(sum(times)/len(times))
