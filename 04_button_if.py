import machine
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

if button.value() == 1:
    print('你有按嗎？')
else:
    print('你有按!')