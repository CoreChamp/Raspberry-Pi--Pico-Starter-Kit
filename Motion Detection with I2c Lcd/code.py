import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
pir_sensor = Pin(15, Pin.IN)

while True:
    reading = pir_sensor.value()
    print(reading)
 
    if reading == 1:
        lcd.putstr("Motion Detect:\n")
        lcd.putstr("Move Detected!")
        utime.sleep(2)
        lcd.clear()
    else:
        lcd.putstr("Motion Detect:\n")
        lcd.putstr("No Move Detect!")
        utime.sleep(2)
        lcd.clear()