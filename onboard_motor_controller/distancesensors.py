from distancesensor import Distance_Sensor

class Distance_Sensors:
    
    DEFAULT_SENSORS = {
        "left": None,
        "right": None,
        "front": None,
        "back": None
        }
    
    DEFAULT_SENSOR_VALUES = {
        "left": 201,
        "right": 201,
        "front": 201,
        "back": 201
        }
    
    def __init__(self, left_sensor = None, right_sensor = None, front_sensor = None, back_sensor = None):
        self.sensors = {
            "left": left_sensor,
            "right": right_sensor,
            "front": front_sensor,
            "back": back_sensor
            }
        self.sensor_values = self.DEFAULT_SENSOR_VALUES
        self.initalizeSensors()
    
    def initalizeSensors(self):
        for sensor in self.sensors:
            if self.sensors[sensor] != None:
                self.sensor_values[sensor] = self.sensors[sensor].gatherData()
        
    def updateSensorValues(self):
        for sensor in self.sensors:
            if self.sensors[sensor] != None:
                self.sensor_values[sensor] = self.sensors[sensor].gatherData()
        
    def getSensorValues(self):
        return self.sensor_values.copy()
    
if __name__ == "__main__":
    sensors = Distance_Sensors(front_sensor = Distance_Sensor(triggerPin = 15, echoPin = 14))
    print(sensors.getSensorValues())