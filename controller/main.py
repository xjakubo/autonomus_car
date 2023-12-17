from serverrequest import Server_Request
from motionsensorreader import Motion_Sensor_Reader
from carstatus import Car_Status
from requestarguments import Request_Arguments
import pygame
import sys

def controllerLoop():
    speed = 0
    direction = 0
    steerprecentage = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        speed = 40
        direction = True
    if keys[pygame.K_a]:
        steerprecentage = -100 
    if keys[pygame.K_s]:
        speed = 40
        direction = False
    if keys[pygame.K_d]:
        steerprecentage = 100 
    if keys[pygame.K_q]:
        speed = 100
        direction = True
    return speed, direction, steerprecentage

car_status = Car_Status()
motion_sensor_reader = Motion_Sensor_Reader()
car = Server_Request("http://192.168.4.1/", car_status,
                     motion_sensor_reader)
requestarguments = Request_Arguments()
car.sendRequest(request_arguments= requestarguments.getRequestArguments())
car.retrieveResponseData()
print(car_status)
pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pilot alpha 0.01")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    speed, direction, steerprecentage = controllerLoop()
    requestarguments.changeSpeed(speed, direction)
    requestarguments.changeDir(steerprecentage)
    car.sendRequest(request_arguments= requestarguments.getRequestArguments())
    car.retrieveResponseData()
