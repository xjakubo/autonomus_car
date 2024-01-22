from server.serverrequest import Server_Request
from server.car.motionsensorreader import Motion_Sensor_Reader
from server.car.carstatus import Car_Status
from server.requestarguments import Request_Arguments
# Zaimportuj RPi_Controller zamiast Pygame_Controller
from controls.rpi_controller import RPi_Controller
import pygame

car_status = Car_Status()
motion_sensor_reader = Motion_Sensor_Reader()
car = Server_Request("192.168.4.1", car_status, motion_sensor_reader)
requestarguments = Request_Arguments()
car.sendRequest(requestarguments= requestarguments.getRequestArguments(),
                is_response_needed=True)
car.retrieveResponseData()

# Inicjalizacja RPi_Controller zamiast Pygame_Controller
controller = RPi_Controller()

while True:
    # controller.checkForOtherEvents() - To jest metoda z Pygame, jeśli chcesz to zachować, musisz zmodyfikować RPi_Controller, aby obsługiwać zdarzenia Pygame.
    speed, direction, steerprecentage = controller.checkForControllerInput()
    requestarguments.changeSpeed(speed, direction)
    requestarguments.changeDir(steerprecentage)
    request = car.sendRequest(requestarguments=requestarguments.getRequestArguments())
    if request == False:
        print("request timeout")
    # car.retrieveResponseData()

    # Dodaj obsługę zdarzenia zatrzymania, jeśli jest potrzebna
    if controller.checkForShutdownEvent():
        print("Shutting down due to shutdown event")
        break

    # Może być konieczne dodanie krótkiego opóźnienia
    pygame.time.delay(10)

# Nie zapomnij o wyczyszczeniu GPIO
controller.cleanup()
