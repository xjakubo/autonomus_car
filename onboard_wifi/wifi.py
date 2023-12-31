import network
import usocket as socket

class Server:
    def __init__(self, ssid: str, password: str):
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid = ssid, password = password, pm = network.WLAN.PM_NONE)
        
    def activateAP(self):
        self.ap.active(True)
        
    def getConfig(self) -> str:
        return self.ap.ifconfig()
    
    def initSocket(self, bindAddr: str) -> socket:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((bindAddr, 80))
        s.listen(5)
        return s
    
    TEST_PAGE = "<html> <head></head> <body><h1> Siemanko </h1></body> </html>"
    
    def accept(self, s: socket) -> tuple:
        return s.accept()
        
    def recieveRequest(self, c: tuple) -> bytes:
        conn,addr = c
        request = b''
        request += conn.recv(1024)
        return request
    
    def recieveStringRequest(self, c: tuple) -> str:
        return self.recieveRequest(c).decode("utf-8")
    
    def decode(self, msg: str) -> dict:
        variables = {}
        parms = msg.split("\n")
        for index, parm in enumerate(parms):
            name = parm.find("Content-Disposition: form-data; name=")
            if name != -1:
                variables[parm[name+38:-2]] = parms[index+2].strip('\r')
        return variables
    
    def response(self, c: tuple, resp: str):
        conn,addr = c
        conn.send(resp)
    
    def close(self, c: tuple):
        conn,addr = c
        conn.close()
    


# ap = network.WLAN(network.AP_IF)
# ap.config(essid = "fastcar", password = "passwd123")
# 
# ap.active(True)

# print(ap.ifconfig())
# def testPage():
#     return "<html> <head></head> <body><h1> Siemanko </h1></body> </html>"

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
#     conn,addr = s.accept()
#     variables = {}
#     print(f'New connection from {addr}')
#     request = conn.recv(1024)
#     request = request.decode("utf-8")
#     parms = request.split("\n")
#     for index, parm in enumerate(parms):
#         name = parm.find("Content-Disposition: form-data; name=")
#         if name != -1:
#             variables[parm[name+38:-2]] = parms[index+2].strip('\r')
#             
#     print(variables)
    
    #parms = request.split("\n")
    #for parm in parms:
        #print(parm)
#     response = testPage()
#     conn.send(response)
#     conn.close()
