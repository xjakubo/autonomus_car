from wifi import Server
from motor import MotorCommunication

m = MotorCommunication()
ap = Server('fastcar','passwd123')
ap.activateAP()
print(ap.getConfig())
s = ap.initSocket('')
while True:
    conn = ap.accept(s)
    msg = ap.decode(ap.recieveStringRequest(conn))
    if 'speed' in msg and 'forward' in msg:
        m.send(int(msg['speed']),bool(msg['forward']))
    ap.response(conn, ap.TEST_PAGE)
    ap.close(conn)