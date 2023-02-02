from machine import Pin, PWM
buzzer = PWM(Pin(7))
buzzer.freq(500)

buzzer.duty_u16(1000)
