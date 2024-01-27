import RPi.GPIO as GPIO
import sys

class Rpi_Controller:
    FRONT_PIN = 37
    BACK_PIN = 33
    LEFT_PIN = 31
    RIGHT_PIN = 29

    def __init__(self):
        self.front_btn = False
        self.back_btn = False
        self.left_btn = False
        self.right_btn = False
        self.setup_GPIO()

    def setup_GPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.FRONT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.BACK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(self.FRONT_PIN, GPIO.BOTH, callback=self.button_callback, bouncetime=300)
        GPIO.add_event_detect(self.BACK_PIN, GPIO.BOTH, callback=self.button_callback, bouncetime=300)
        GPIO.add_event_detect(self.LEFT_PIN, GPIO.BOTH, callback=self.button_callback, bouncetime=300)
        GPIO.add_event_detect(self.RIGHT_PIN, GPIO.BOTH, callback=self.button_callback, bouncetime=300)

    def button_callback(self, channel):
        if channel == self.FRONT_PIN:
            self.front_btn = GPIO.input(self.FRONT_PIN)
        elif channel == self.BACK_PIN:
            self.back_btn = GPIO.input(self.BACK_PIN)
        elif channel == self.LEFT_PIN:
            self.left_btn = GPIO.input(self.LEFT_PIN)
        elif channel == self.RIGHT_PIN:
            self.right_btn = GPIO.input(self.RIGHT_PIN)


    def checkForControllerInput(self) -> tuple:
        speed = 0
        direction = 0
        steerprecentage = 0
        keys = pygame.key.get_pressed()
        if self.front_btn:
            speed = 40
            direction = True
        if self.left_btn:
            steerprecentage = -100
        if self.back_btn:
            speed = 40
            direction = False
        if self.right_btn:
            steerprecentage = 100
        return speed, direction, steerprecentage

