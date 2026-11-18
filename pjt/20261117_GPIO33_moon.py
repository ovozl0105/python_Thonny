from machine import Pin
import time

RED_LED = 33
FLASH_LED = 4
ON_LED = 1
OFF_LED = 0.5

led = Pin(RED_LED, Pin.OUT, value=1)
for led_cnt in range(10) :
    led.value(0)
    time.sleep(ON_LED)
    led.value(1)
    time.sleep(OFF_LED)
