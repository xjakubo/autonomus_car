from machine import PWM, Pin
class Motor:
    
    def __init__(self):
        self.m1 = Pin(21, Pin.OUT)
        self.m2 = Pin(20, Pin.OUT)
    
        self.MINIMAL_DUTY = 3000
        self.MAXIMAL_DUTY = 65000
        self.pwm1 = PWM(self.m1)
        self.pwm2 = PWM(self.m2)
        self.pwm1.freq(1000)
        self.pwm2.freq(1000)
        self.pwm1.duty_u16(self.MAXIMAL_DUTY)
        self.pwm2.duty_u16(self.MAXIMAL_DUTY)

        self.en1 = Pin(17, Pin.OUT)
        
    def calculateDuty(self, procent: int) -> int:
        if procent <= 0:
            return 0
        elif procent >= 100:
            return self.MAXIMAL_DUTY
        return int(((self.MAXIMAL_DUTY - self.MINIMAL_DUTY)/100)*procent)

    def enable(self):
        self.en1(1)  # motor 1 enable, set value 0 to disable
        
    def disable(self):
        self.en1(0)

    def forward(self, speed: int):
        self.pwm1.duty_u16(self.calculateDuty(speed))
        self.pwm2.duty_u16(0)
    
    def reverse(self, speed: int):
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(self.calculateDuty(speed))
        
    def move(self, instructions: tuple):
        if instructions[0]:
            self.forward(instructions[1])
            return
        self.reverse(instructions[1])
    
    def stop(self):
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
    