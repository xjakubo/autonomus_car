import RPi.GPIO as GPIO

class ControllerInput:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # Użyj numeracji BCM dla pinów

        self.buttons = {
            'forward': 17,
            'left': 27,
            'backward': 22,
            'right': 23,
            'boost': 24
        }

        # Ustaw piny jako wejście z rezystorami podciągającymi do VCC
        for button, pin in self.buttons.items():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def checkForControllerInput(self):
        speed = 0
        direction = 0
        steerpercentage = 0

        # Odczytaj stan przycisków i zaktualizuj zmienne sterujące
        if not GPIO.input(self.buttons['forward']):  # Przycisk do przodu
            speed = 40
            direction = True

        if not GPIO.input(self.buttons['left']):  # Przycisk w lewo
            steerpercentage = -100

        if not GPIO.input(self.buttons['backward']):  # Przycisk do tyłu
            speed = 40
            direction = False

        if not GPIO.input(self.buttons['right']):  # Przycisk w prawo
            steerpercentage = 100

        if not GPIO.input(self.buttons['boost']):  # Przycisk boost
            speed = 100
            direction = True

        return speed, direction, steerpercentage

    def cleanup(self):
        # Metoda do czyszczenia konfiguracji GPIO przed zamknięciem programu
        GPIO.cleanup()
