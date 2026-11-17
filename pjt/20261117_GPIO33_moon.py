from machine import Pin
import time

led = Pin(33, Pin.OUT, value=1)

for led_cnt in range(10) :
    led.value(0)
    time.sleep(1)
    led.value(1)
    time.sleep(1)
