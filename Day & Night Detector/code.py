import utime
from machine import I2C, Pin

ldr_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if ldr_sensor.value() == 1:
       print("Night Detected")
       utime.sleep(3)
   else:
       print("Day Detected")
       utime.sleep(1)
utime.sleep(0.1)
