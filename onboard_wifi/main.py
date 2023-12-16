from wifi import Server
from motor import MotorCommunication
import json
import gc
import machine

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
    m.send(msg)
    ap.response(conn, msg)
    ap.close(conn)
    #if m.checkForCommunication():
        #print(str(m.read()))
