
class Car_Status:

    SPEED = "speed"
    DRIVE_DIRECTION = "drive_direction"
    STEER_DIRECTION = "steer_direction"
    DEFAULT_CAR_STATUS = {
        SPEED : 0,
        DRIVE_DIRECTION : True,
        STEER_DIRECTION : 0
    }

    def __init__(self):
        self.carStatus = self.DEFAULT_CAR_STATUS

    def updateStatus(self, speed:int, driveDirection: bool, steerDirection: int):
        self.carStatus[self.SPEED] = speed
        self.carStatus[self.DRIVE_DIRECTION] = driveDirection
        self.carStatus[self.STEER_DIRECTION] = steerDirection

    def getStatus(self):
        return self.carStatus.copy()
    
    def getSpeed(self):
        return self.carStatus[self.SPEED]

    def getDriveDirection(self):
        return self.carStatus[self.DRIVE_DIRECTION]

    def getSteerDirection(self):
        return self.carStatus[self.STEER_DIRECTION]
