from machine import Pin
import utime

rain_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if rain_sensor.value() == 1:
       print("Rain Detected")
       utime.sleep(3)
   else:
       print("No Rain")
       utime.sleep(1)
utime.sleep(0.1)