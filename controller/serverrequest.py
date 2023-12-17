from requestarguments import Request_Arguments
import requests, json
from carstatus import Car_Status
from motionsensorreader import Motion_Sensor_Reader

class Server_Request:

    TIMEOUT = 5
    car_status: Car_Status
    motion_sensor_reader: Motion_Sensor_Reader

    def __init__(self, serverUrl: str,
                 car_status: Car_Status,
                 motion_sensor_reader: Motion_Sensor_Reader):
        self.server_url = serverUrl
        self.car_status = car_status
        self.motion_sensor_reader = motion_sensor_reader


    def sendRequest(self, request_arguments: dict):
        self.request = requests.post(url = self.server_url,
                                    json = request_arguments,
                                    timeout = self.TIMEOUT
                                    )

    def tryResponseToJson(self):
        try:
            jsondata = self.request.json()
            print(jsondata)
            return jsondata
        except ValueError:
            return None

    def retrieveResponseData(self):
        if self.request.status_code != 200:
            return None
        response_json = self.tryResponseToJson()
        if response_json == None:
            return None
        if 'car' in response_json:
            self.responseToCarStatus(json_data['car'])
        if 'sensor' in response_json:
            self.reponseToMotionSensorStatus(json_data['sensors'])

    def responseToCarStatus(self, json):
       self.car_status.updateStatus(json['speed'], json['drive_direction'],
                                   json['steer_direction'])

    def reponseToMotionSensorStatus(self, json):
        self.motion_sensor_reader.updateStatus(json['front'], json['back'],
                                               json['left'], json['right'])

