from machine import Pin, UART
from time import sleep,time

uart = UART(1, baudrate=9600, tx=Pin(4), rx = Pin(5))
uart.init(bits=8, parity = None, stop = 2)
errorStatusLed = Pin(21, Pin.OUT)
okStatusLed = Pin(20, Pin.OUT)
progressLed = Pin(19, Pin.OUT)
rightBtn = Pin(27, Pin.IN)
leftBtn = Pin(26, Pin.IN)

class Serial_Communication:
    
    def __init__(self, baudrate, txPin, rxPin):
        self.uart = UART(1, baudrate=baudrate, tx=Pin(txPin), rx = Pin(rxPin))
        self.uart.init(bits=8, parity = None, stop = 2)
        pass
    
    def checkForIncomingPayload(self) -> bool:
        return self.uart.any()
    
    def retrieveFromSerial(self) -> str:
        payload = uart.readline()
        return str(payload)
    
    def isOperationSucessful(self, status: str) -> int:
            pass
    
    def sendIntegerToSerial(self, integer: int) -> bool:
        preparedInteger = str(integer)
        self.uart.write(preparedInteger)
        return True
    
    def sendMessageToSerial(self, message: str) -> bool:
        preparedMessage = str.encode(message)
        self.uart.write(preparedMessage)
        
class Servo_Controller:
    
    TIME_TILL_FAIL = 10
    
    def __init__(self):
        self.serial = Serial_Communication(9600,4,5)
    
    def rotate(self, angle: int):
        self.serial.sendMessageToSerial('m')
        self.serial.sendIntegerToSerial(angle)
        
    def __checkStatus(self) -> str:
        if self.serial.checkForIncomingPayload():
            status = self.serial.retrieveFromSerial()
            print(status)
            if status == 'o':
                return "ok"
            elif status == 'f':
                return "fail"
        return "processing"
                    
    def waitForStatus(self) -> str:
        status = self.__checkStatus()
        startTime = time()
        while True:
            if status == "ok" or status == "fail":
                return status
            elif status == "processing":
                status = self.__checkStatus()
            else:
                print("Blad! niepoprawna wartosc!")
                print(status)
            if time() - startTime >= self.TIME_TILL_FAIL:
                return "error"
                
    
class Led_Status:
    
    def __init__(self, okStatusLed:int, errorStatusLed:int, progressLed:int):
        self.okStatusLed = Pin(okStatusLed, Pin.OUT)
        self.errorStatusLed = Pin(errorStatusLed, Pin.OUT)
        self.progressLed = Pin(progressLed, Pin.OUT)
        
    def switchProgressLed(self, value:bool) -> None:
        self.reset()
        if value:
            self.progressLed.value(1)
        else:
            self.progressLed.value(0)
            
    def setStatus(self, status:str) -> bool:
        self.reset()
        if status == "ok":
            self.okStatusLed.value(1)
            return True
        elif status == "fail":
            self.errorStatusLed.value(1)
            return True
        elif status == "error":
            self.showError()
            return True
        else:
            return False
        
    def showError(self) -> None:
        self.reset()
        for i in range(5):
            self.errorStatusLed.value(1)
            sleep(0.1)
            self.errorStatusLed.value(0)
            sleep(0.1)
        
    def reset(self) -> None:
        self.okStatusLed.value(0)
        self.errorStatusLed.value(0)
        self.progressLed.value(0)
        
class Input:
    
    def __init__(self, rightBtnPin:int, leftBtnPin:int):
        self.rightBtnPin = Pin(rightBtnPin, Pin.IN)
        self.leftBtnPin = Pin(leftBtnPin, Pin.IN)
        self.rotationAngle = 20
    
    def checkButtonInput(self) -> int:
        if self.rightBtnPin.value() == 1:
            return self.rotationAngle
        elif self.leftBtnPin.value() == 1:
            return -(self.rotationAngle)
        else:
            return 0


def main():
    pilot = Input(26,27)
    ledStatus = Led_Status(20,21,19)
    servo = Servo_Controller()
    
    while True:
        angle = pilot.checkButtonInput()
        if angle != 0:
            sleep(1)
            ledStatus.switchProgressLed(True)
            servo.rotate(angle)
            status = servo.waitForStatus()
            ledStatus.setStatus(status)
        
main()
# while True:
#     uart.write('1')
#     if uart.any():
#         data = uart.read()
#         if data == b'0':
#             led.toggle()
#     sleep(1)