import machine
#PULL_UP : pin 12 = 高電位 ，按鈕另一端需要接 GND
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
#沒按執行後為 1 ; 按著執行為 0
print(button.value())