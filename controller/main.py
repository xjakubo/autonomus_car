from server.serverrequest import Server_Request
from server.car.motionsensorreader import Motion_Sensor_Reader
from server.car.carstatus import Car_Status
from server.requestarguments import Request_Arguments
from userinterface.userinterface import User_Interface 
from controls.rpicontroller import Rpi_Controller

controller = Rpi_Controller()
car_status = Car_Status()
motion_sensor_reader = Motion_Sensor_Reader()
car = Server_Request("192.168.4.1", car_status,
                     motion_sensor_reader)
requestarguments = Request_Arguments()
car.sendRequest(request_arguments= requestarguments.getRequestArguments(),
                is_response_needed = True)
car.retrieveResponseData()
ui = User_Interface()
ui.setupDisplay("Autonomus Car v0.1")


while True:
    speed, direction, steerprecentage = controller.checkForControllerInput()
    requestarguments.changeSpeed(speed, direction)
    requestarguments.changeDir(steerprecentage)
    request = car.sendRequest(request_arguments= requestarguments.getRequestArguments())
    if request == False:
        print("request timeout")
    #car.retrieveResponseData()
