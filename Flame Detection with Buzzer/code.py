from machine import Pin, PWM
import utime
 
flame_sensor = Pin(16, Pin.IN)
buzzer = Pin(17, Pin.OUT)
utime.sleep(0.5)
 
while True:
    while flame_sensor.value() == 1:
        print("Flame Detected")
        buzzer.high()    
    if flame_sensor.value() == 0:
        buzzer.low()
        print("No Flame")
 
utime.sleep(0.2)