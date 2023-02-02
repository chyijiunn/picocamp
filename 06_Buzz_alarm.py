from machine import Pin, PWM , ADC
from utime import sleep

buzz = PWM(Pin(7))
buzz.freq(500)

˚C = 27 - (ADC(4).read_u16()* 3.3 / 65535 - 0.706) / 0.001721
print(˚C)
if ˚C > 15:
    buzz.duty_u16(1000)
    sleep(3)
    buzz.duty_u16(0)
    print(˚C)