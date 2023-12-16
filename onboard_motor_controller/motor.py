from machine import PWM, Pin
class Motor:

    def __init__(self, enablePin = 17, forwardPin = 21, reversePin = 20):
        self.forward_motor = Pin(forwardPin, Pin.OUT)
        self.reverse_motor = Pin(reversePin , Pin.OUT)

        self.MINIMAL_DUTY = 3000
        self.MAXIMAL_DUTY = 65000
        self.forward_pwm = PWM(self.forward_motor)
        self.reverse_pwm = PWM(self.reverse_motor)
        self.forward_pwm.freq(1000)
        self.reverse_pwm.freq(1000)
        self.forward_pwm.duty_u16(self.MAXIMAL_DUTY)
        self.reverse_pwm.duty_u16(self.MAXIMAL_DUTY)

        self.enable_motor = Pin(enablePin, Pin.OUT)

    def calculateDuty(self, procent: int) -> int:
        if procent <= 0:
            return 0
        elif procent >= 100:
            return self.MAXIMAL_DUTY
        return int(((self.MAXIMAL_DUTY - self.MINIMAL_DUTY)/100)*procent)

    def enable(self):
        self.enable_motor(1)  # motor 1 enable, set value 0 to disable

    def disable(self):
        self.enable_motor(0)

    def forward(self, speed: int):
        self.forward_pwm.duty_u16(self.calculateDuty(speed))
        self.reverse_pwm.duty_u16(0)

    def reverse(self, speed: int):
        self.forward_pwm.duty_u16(0)
        self.reverse_pwm.duty_u16(self.calculateDuty(speed))

    def move(self, instructions: tuple):
        if instructions[0]:
            self.forward(instructions[1])
            return
        self.reverse(instructions[1])

    def stop(self):
        self.forward_pwm.duty_u16(0)
        self.reverse_pwm.duty_u16(0)

