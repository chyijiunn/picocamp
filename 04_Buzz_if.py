from machine import Pin, PWM
from utime import sleep

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer = PWM(Pin(7))
buzzer.freq(500)

if button.value() == 0:
    buzzer.duty_u16(1000)