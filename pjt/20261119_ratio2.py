from machine import Pin
import time

LED_PIN = 4
ON_VALUE = 1
OFF_VALUE = 0
PERIOD = 0.01

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)

while True:
    for level in range (0, 11, 1):
        ratio = level / 10
        on_time = PERIOD * ratio
        off_time = PERIOD - on_time
        led.value(ON_VALUE)
        time.sleep(on_time)
        led.value(OFF_VALUE)
        time.sleep(off_time)
        
    for level in range (100, 0, -1):
        ratio = level / 100
        on_time = PERIOD * ratio
        off_time = PERIOD - on_time
        led.value(ON_VALUE)
        time.sleep(on_time)
        led.value(OFF_VALUE)
        time.sleep(off_time)
    