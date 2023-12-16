from motors import Motors


motors = Motors()
motors.initalizeMotor(motors.LEFT_MOTOR, 17, 21, 20)
motors.initalizeMotor(motors.RIGHT_MOTOR, 16, 19, 18)

def motorTurnInTest(turn_value: int):
    print(f'Right turn: {motors.calculateTurnPrecentage(25, turn_value)}')
    print(f'Left turn: {motors.calculateTurnPrecentage(25, -turn_value)}')


motorTurnInTest(int(input("Turn in radius test: ")))

