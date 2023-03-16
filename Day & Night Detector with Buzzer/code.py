from machine import Pin, PWM
import utime
 
ldr_sensor = Pin(16, Pin.IN)
led = Pin(17, Pin.OUT)
utime.sleep(0.5)
 
while True:
    while ldr_sensor.value() == 1:
        print("Night Detected")
        led.high()    
    if flame_sensor.value() == 0:
        led.low()
        print("Day Detected")
 
utime.sleep(0.2)