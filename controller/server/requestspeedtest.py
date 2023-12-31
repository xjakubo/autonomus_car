from time import time,sleep
from requestarguments import Request_Arguments
from serverrequest import Server_Request
from .car.motionsensorreader import Motion_Sensor_Reader
from .car.carstatus import Car_Status
import random


url = "192.168.4.1"
arguments = Request_Arguments()
times = []
car_status = Car_Status()
motion_sensor_reader = Motion_Sensor_Reader()
server = Server_Request(url, car_status, motion_sensor_reader)
print("starting test")
while len(times) < 100:
    start = time()
    arguments.changeSpeed(random.randint(1,100), random.choice([True,False]))
    arguments.changeDir(random.randint(-100,100))
    server.sendRequest(arguments.getRequestArguments())
    if len(times) % 10 == 0:
        server.retrieveResponseData()
    print(f"{len(times)} request OK")
    #print(car_status.getStatus())
    sleep(0.1)
    times.append(time() - start)


arguments.changeSpeed(0, True)
arguments.changeDir(0)
server.sendRequest(arguments.getRequestArguments())
print(sum(times)/len(times))
