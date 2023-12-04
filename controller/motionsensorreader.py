

class Motion_Sensor_Reader:

    FRONT_SENSOR = "front"
    BACK_SENSOR = "back"
    RIGHT_SENSOR = "right"
    LEFT_SENSOR = "left"

    DEFAULT_SENSOR_READ={
        FRONT_SENSOR : 0,
        BACK_SENSOR : 0,
        RIGHT_SENSOR : 0,
        LEFT_SENSOR : 0
    }

    def __init__(self):
       self.sensor_read = self.DEFAULT_SENSOR_READ

    def updateStatus(self, front_sensor: int, back_sensor: int, left_sensor:
                     int, right_sensor: int):
        self.sensor_read[self.FRONT_SENSOR] = front_sensor
        self.sensor_read[self.BACK_SENSOR] = back_sensor
        self.sensor_read[self.RIGHT_SENSOR] = right_sensor
        self.sensor_read[self.LEFT_SENSOR] = left_sensor

    def getSensorRead(self):
        return self.sensor_read.copy()
