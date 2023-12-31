

class Info_Screen:

    SPEED = "SPEED"
    SENSORS = "SENSORS"
    SENSOR_STATUS = "SENSOR_STATUS"
    CONNECTION_STATUS = "CONNECTION_STATUS"

    DEFAULT_MENU_VALUES = {
        SPEED: 0,
        SENSORS: {},
        SENSOR_STATUS: False,
        CONNECTION_STATUS : False
    }
    def __init__(self):
        self.menu_values = self.DEFAULT_MENU_VALUES
        pass

    def retrieveMenuValues(self) -> dict:
        return self.menu_values.copy()

    def setSpeed(self, speed):
        self.menu_values[self.SPEED] = speed

if __name__ == "__main__":
    infoscreen = Info_Screen()
    print(infoscreen.retrieveMenuValues())
