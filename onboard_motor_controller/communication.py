from machine import UART
import json
class Communication:
    
    uart: UART
    
    def __init__(self, baudrate: int, txpin: Pin, rxpin: Pin):
        self.baudrate = baudrate
        self.txpin = txpin
        self.rxpin = rxpin
    
    def initalizeUart(self):
        self.uart = UART(1, baudrate=self.baudrate, tx=self.txpin, rx=self.rxpin)
        self.uart.init(bits=8, parity=None, stop=2)
        
    def readFromBuffer(self) -> str:
        message = self.uart.read()
        print(f'raw message: {message}')
        message = message.decode('utf-8')
        print(f'decoded message: {message}')
        return message[:message.find('}')+1]
    
    def decodeMessageToArguments(self, message: str) -> dict:
        if len(message) == 0:
            print("zero on uart!")
            return None
        try:
            msg = json.loads(message)
        except ValueError as e:
            print(e)
            return None
        return msg
    
    def send(self, msg: str):
        self.uart.write(msg)
        
    def checkForMessageType(self, arguments: dict) -> str:
        if "speed" in arguments:
            return "control"
        return "unknown"
        pass

    def checkForCommunication(self) -> bool:
        if self.uart.any():
            return True
        return False
