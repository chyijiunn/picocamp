from machine import Pin, I2C,PWM
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread

buzzer = PWM(Pin(7))
buzzer.freq(500)
i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buttonR = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1
buttonL = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

oled.fill(0)

x = 64
y = 32
button_caculation = 0
path =[]
def draw():
    data = open('trunk','r')
    for line in data:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            oled.pixel(xAxis,yAxis,1)
    data.close()

def button_thread():
    global button_caculation
    while True:
        if buttonR.value() == 0:button_caculation = button_caculation + 1
        if buttonL.value() == 0:button_caculation = button_caculation - 1
        if buttonR.value() == 0 and buttonL.value() == 0:break
        sleep(0.1)    
_thread.start_new_thread(button_thread, ())

while True: 
    if x > 128: x =0
    if x <0: x = 128
    if y > 64 : y =0
    if y <0 : y = 64
    if button_caculation % 4 == 0:x = x + 1
    if button_caculation % 4 == 1:y = y + 1
    if button_caculation % 4 == 2:x = x - 1
    if button_caculation % 4 == 3:y = y - 1
    if buttonR.value() == 0 and buttonL.value() == 0:break
    oled.pixel(x,y,1)
    if [x,y] in path:
        buzzer.duty_u16(1000)
        draw()
        break
    oled.show()
    path.append([x,y])