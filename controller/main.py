from serverrequest import Server_Request
from motionsensorreader import Motion_Sensor_Reader
from carstatus import Car_Status
from requestarguments import Request_Arguments

LOOP_STATUS = True

def controllerLoop():
    while LOOP_STATUS:
        pass



def main():
    car_status = Car_Status()
    motion_sensor_reader = Motion_Sensor_Reader()
    car = Server_Request("http://192.168.4.1/", car_status,
                         motion_sensor_reader)
    requestarguments = Request_Arguments()
    car.sendRequest(request_arguments= requestarguments.getRequestArguments())
    car.retrieveResponseData()
    print(car_status)
main()


