from machine import Pin
from motors import Motors
from communication import Communication
from carstatus import Car_Status
from distancesensors import Distance_Sensors
from distancesensor import Distance_Sensor
import time
import json


def updateSensors(sensors: Distance_Sensors):
    sensors.updateSensorValues()

def initalizeMotors():
    motors = Motors()
    motors.initalizeMotor(motors.LEFT_MOTOR, 17, 21, 20)
    motors.initalizeMotor(motors.RIGHT_MOTOR, 16, 19, 18)
    return motors

def initalizeDistanceSensors():
    distance_sensors = Distance_Sensors(
    #front_sensor = Distance_Sensor(triggerPin = 15, echoPin = 14)
    )
    return distance_sensors

def initalizeUart():
    uart = Communication(115200, Pin(4), Pin(5))
    time.sleep(1)
    uart.initalizeUart()
    return uart

def generateResponse():
    response["car"] = car_status.getCarStatus()
    if distance_sensors != None:
        response["sensors"] = distance_sensors.getSensorValues()
    return json.loads(response)

motors = initalizeMotors()
distance_sensors = initalizeDistanceSensors()
uart = initalizeUart()
car_status = Car_Status()
response = {}
uart_arguments = None
while True:
    #updateSensors(distance_sensors)
    if uart.checkForCommunication():
        uart_arguments = uart.decodeMessageToArguments(uart.readFromBuffer())
        print(f'uart_arguments = {uart_arguments}')
        if uart_arguments != None and uart.checkForMessageType(uart_arguments) == "control":
            car_status.setCarStatus(uart_arguments)
            instructions = car_status.getCarStatus()
            motors.move(instructions[car_status.SPEED],
                       instructions[car_status.DRIVE_DIRECTION],
                      instructions[car_status.STEER_DIRECTION])
        uart.send(generateResponse())
