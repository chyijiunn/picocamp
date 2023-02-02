import machine
import utime

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 1:
        print('你有按嗎？')
    else:
        print('你有按!')