
class Request_Arguments:

    SPEED = "speed"
    DRIVE_DIRECTION = "drive_direction"
    STEER_DIRECTION = "steer_direction"
    START_ARGUMENTS ={
        SPEED: 0,
        DRIVE_DIRECTION: True,
        STEER_DIRECTION: 0
    }

    def __init__(self):
        self.requestArguments = self.START_ARGUMENTS
        pass

    def changeSpeed(self, speedPrecentage: int, driveDirection: bool):
        if speedPrecentage not in range(-100,100):
            return
        self.requestArguments[self.SPEED] = speedPrecentage
        self.requestArguments[self.DRIVE_DIRECTION] = driveDirection

    def changeDir(self, dirPrecentage: int):
        if dirPrecentage not in range(-100,101):
            return
        self.requestArguments[self.STEER_DIRECTION] = dirPrecentage

    def getRequestArguments(self):
        return self.requestArguments.copy()
