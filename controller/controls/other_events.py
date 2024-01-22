import RPi.GPIO as GPIO
import time

class OtherEvents:
    def __init__(self, stop_button_pin):
        self.stop_button_pin = stop_button_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.stop_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.previous_button_state = True

    def checkForShutdownEvent(self):
        # Odczytaj stan przycisku zatrzymania
        button_state = GPIO.input(self.stop_button_pin)
        if button_state == False and self.previous_button_state == True:
            # Przycisk został naciśnięty
            print("Shutdown button pressed")
            time.sleep(0.5)  # Proste odbicie przycisku
            return True
        self.previous_button_state = button_state
        return False

    def cleanup(self):
        # Metoda do czyszczenia konfiguracji GPIO przed zamknięciem programu
        GPIO.cleanup()
