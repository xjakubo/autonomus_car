from machine import Pin
import utime
import gc


OPERATIONS_PER_CYCLE = 5
MAX_DISTANCE = 200

class Distance_Sensor:
    trigger: int
    echo: int
    
    def __init__(self, triggerPin, echoPin):
        self.trigger = Pin(triggerPin, Pin.OUT)
        self.echo = Pin(echoPin, Pin.IN)
        
    def measureDistance(self) -> int:
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        while self.echo.value() == 0:
            offtime = utime.ticks_us()
        while self.echo.value() == 1:
            ontime = utime.ticks_us()
        timepassed = ontime - offtime
        distance = (timepassed * 0.0343) / 2
        return distance


    def normaliseBadMeasurements(self, data, threshold):
        return [val for val in data if val < threshold]

    def average(self, data):
        if len(data) == 0:
            return MAX_DISTANCE
        average = sum(data)/len(data)
        return int(average)

    def gatherData(self):
        data = []
        for i in range(OPERATIONS_PER_CYCLE):
           data.append(self.measureDistance())
        distance = self.normaliseBadMeasurements(data, MAX_DISTANCE)
        return self.average(distance)
        #print(f'Distance: {distance} without Outliers {distance - distance_unfiltered}')

    def benchmark(self):    
        start = utime.time()
        counter = 0
        while utime.time() - start < 10:
            counter += 1
            self.gatherData()
        return counter/10

if __name__ == "__main__":
    front = Distance_Sensor(triggerPin = 15, echoPin = 14)
    print(f'Operations per second {front.benchmark()}')

#test()