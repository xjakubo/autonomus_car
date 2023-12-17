from motor import Motor

class Motors:

    LEFT_MOTOR = "left"
    RIGHT_MOTOR = "right"
    DEFAULT_MOTOR_PLACEMENT = {
        LEFT_MOTOR : None,
        RIGHT_MOTOR : None
    }

    def __init__(self):
        self.motor_placement = self.DEFAULT_MOTOR_PLACEMENT

    def initalizeMotor(self, placement, enable_pin, forward_pin, reverse_pin):
        if placement not in self.motor_placement:
            return None
        self.motor_placement[placement] = Motor(enable_pin, forward_pin,
                                                reverse_pin)
        self.motor_placement[placement].enable()
        return self.motor_placement[placement]


    def calculateTurnPrecentage(self, speed: int, turn_value: int):
        left_precentage = speed
        right_precentage = speed
        if speed == 0:
            return (left_precentage, right_precentage)
        if turn_value < 0:
            left_precentage = int(abs(turn_value)/(100/speed))
            return (left_precentage, right_precentage)
        right_precentage = int(turn_value/(100/speed))
        return (left_precentage, right_precentage)

    def move(self, speed: int, drive_direction: bool, turn_value: int):
        if turn_value == 0:
            self.motor_placement[self.LEFT_MOTOR].move((drive_direction, speed))
            self.motor_placement[self.RIGHT_MOTOR].move((drive_direction, speed))
            return
        if turn_value == -100:
            self.motor_placement[self.LEFT_MOTOR].move((not drive_direction,
                                                        speed))
            self.motor_placement[self.RIGHT_MOTOR].move((drive_direction, speed))
        if turn_value == 100:
            self.motor_placement[self.LEFT_MOTOR].move((drive_direction,
                                                        speed))
            self.motor_placement[self.RIGHT_MOTOR].move((not drive_direction, speed))
        left_precentage, right_precentage = self.calculateTurnPrecentage(speed, turn_value)
        self.motor_placement[self.LEFT_MOTOR].move((drive_direction,
                                                    left_precentage))
        self.motor_placement[self.RIGHT_MOTOR].move((drive_direction,
                                                     right_precentage))

    def getMotorValues(self):
        return self.motor_placement.copy()
