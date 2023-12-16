from machine import UART, Pin
import json

class MotorCommunication:
    
    def __init__(self):
        self.uart = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
        
    def initializeUart(self):
        self.uart.init(bits=8, parity=None, stop=2)
    
    def send(self, message: dict):
        #msg = json.dumps(message)
        print(message)
        print(self.uart.write(message))
        
    def read(self) -> str:
        return self.uart.read()
        
    def checkForCommunication(self) -> bool:
        if self.uart.any():
            return True
        return False
#     
# car = {
# 	"speed": 100,
# 	"drive_direction": True,
# 	"steer_direction": 50
# }
# 
# 
# m = MotorCommunication()
# m.send(car)
