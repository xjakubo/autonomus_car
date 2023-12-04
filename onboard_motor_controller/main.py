from machine import Pin
from motor import Motor
from communication import Communication
from carstatus import Car_Status
from distancesensors import Distance_Sensors
from distancesensor import Distance_Sensor
import time
import json


def updateSensors(sensors: Distance_Sensors):
    sensors.updateSensorValues()

led = Pin(25, Pin.OUT)
       
motor = Motor()
motor.enable()
uart = Communication(9600, Pin(4), Pin(5))
uart.initalizeUart()
car_status = Car_Status()
motor.move((True,100))
time.sleep(1)

response = {}
#declare distance sensors if needed
distance_sensors = Distance_Sensors(
    front_sensor = Distance_Sensor(triggerPin = 15, echoPin = 14)
    )
uart_arguments = None
while True:
    updateSensors(distance_sensors)
    if uart.checkForCommunication():
        uart_arguments = uart.decodeMessageToArguments(uart.readFromBuffer())
        print(f'uart_arguments = {uart_arguments}')
        if uart_arguments != None and "speed" in uart_arguments:
            led.toggle()
            car_status.setCarStatus(uart_arguments)
            instructions = car_status.getMotorInstructions()
            motor.move(instructions)
        response["car"] = car_status.getCarStatus()
        if distance_sensors != None:
            response["sensors"] = distance_sensors.getSensorValues()
        print(response)
        uart.send(json.dumps(response))
