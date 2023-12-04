from wifi import Server
from motor import MotorCommunication
import json
import gc
#import machine

'''
from time import sleep
message = '{"speed": 10, "drive_direction": true, "steer_direction": 0}'
messagetw = '{"speed": 100, "drive_direction": true, "steer_direction": 0}'
m = MotorCommunication()
m.initializeUart()

while True:
    m.send(message)
    sleep(1)
    m.send(messagetw)
    sleep(1)
'''

m = MotorCommunication()
ap = Server('fastcar','passwd123')
ap.activateAP()
print(ap.getConfig())
status = ap.initSocket('')
counter = 0
    
machine.freq(250000000)
m.initializeUart()

while True:
    counter += 1
    conn = ap.accept(status)
    msg = ap.recieveStringRequest(conn)
    print(msg)
    m.send(msg)
    #if 'speed' in msg and 'forward' in msg:
        #m.send(int(msg['speed']),bool(msg['forward']))
    ap.response(conn, msg)
    ap.close(conn)
    if m.checkForCommunication():
        print(str(m.read()))
