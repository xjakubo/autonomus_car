from motor import MotorCommunication
from time import sleep

message = '{"speed": 10, "drive_direction": True, "steer_direction": 0}'
messagetw = '{"speed": 100, "drive_direction": True, "steer_direction": 0}'

m = MotorCommunication()

while True:
    m.send(message)
    sleep(1)
    m.send(messagetw)
    sleep(1)