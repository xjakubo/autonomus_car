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
        self.car_status = self.DEFAULT_CAR_STATUS
        
    def getCarStatus(self) -> dict:
        return self.car_status.copy()
    
    def getMotorInstructions(self) -> tuple:
        return (self.car_status[self.DRIVE_DIRECTION], self.car_status[self.SPEED])
    
    def setCarStatus(self, json: dict):
        self.car_status[self.SPEED] = json[self.SPEED]
        self.car_status[self.DRIVE_DIRECTION] = json[self.DRIVE_DIRECTION]
        self.car_status[self.STEER_DIRECTION] = json[self.STEER_DIRECTION]