from .requestarguments import Request_Arguments
import socket, json
from .car.carstatus import Car_Status
from .car.motionsensorreader import Motion_Sensor_Reader

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

    def initalizeSocket(self) -> socket.socket:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(self.TIMEOUT)
        address = (self.server_url, 80)
        try:
            client_socket.connect(address)
        except socket.timeout:
            return None
        return client_socket

    def sendRequest(self, request_arguments: dict, is_response_needed = False) -> bool:
        self.client_socket = self.initalizeSocket()
        if self.client_socket == None:
            return False
        json_data = json.dumps(request_arguments).encode('utf-8')
        self.client_socket.sendall(json_data)
        if is_response_needed == False:
            self.client_socket.close()
        return True

    def tryResponseToJson(self):
        try:
            jsondata = json.loads(self.client_socket.recv(1024).decode())
            print(f'response = {jsondata}')
            return jsondata
        except ValueError as e:
            print(e)
            return None

    def retrieveResponseData(self):
        if self.client_socket == None:
            return None
        response_json = self.tryResponseToJson()
        if response_json == None:
            return None
        if 'car' in response_json:
            self.responseToCarStatus(json_data['car'])
        if 'sensor' in response_json:
            self.reponseToMotionSensorStatus(json_data['sensors'])
        self.client_socket.close()    

    def responseToCarStatus(self, json):
       self.car_status.updateStatus(json['speed'], json['drive_direction'],
                                   json['steer_direction'])

    def reponseToMotionSensorStatus(self, json):
        self.motion_sensor_reader.updateStatus(json['front'], json['back'],
                                               json['left'], json['right'])

