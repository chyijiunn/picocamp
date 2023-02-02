from machine import Pin, I2C
from ssd1306 import SSD1306_I2C#安裝 ssd1306

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

oled.text('hello',0,0)
oled.text('hello2',0,10)#文字放在 (0,10)
oled.line(0,0,128,64,1)#畫一條線 from(x0,y0,x1,y1,1)
oled.pixel(64,32,1)#放一個點在 (64,32)

oled.show()