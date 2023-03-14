from machine import I2C, Pin
import utime as time
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht import DHT11, InvalidChecksum

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    time.sleep(5)
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Temp.: {}".format(sensor.temperature))
    lcd.move_to(0,1)
    time.sleep(5)
    lcd.putstr("Humidity: {}".format(sensor.humidity))
    time.sleep(2)
