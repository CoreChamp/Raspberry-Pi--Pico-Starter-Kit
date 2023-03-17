from machine import Pin, PWM
import utime
 
rain_sensor = Pin(16, Pin.IN)
buzzer = Pin(17, Pin.OUT)
utime.sleep(0.5) 
while True:
    while rain_sensor.value() == 1:
        print("Rain Detected")
        buzzer.high()
    
    if rain_sensor.value() == 0:
                
        buzzer.low()
        print("No Rain")
 
utime.sleep(0.2)