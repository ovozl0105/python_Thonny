from  machine import Pin
import time

RED_LED = 33
FLASH_LED = 4

ON_LED = 0.001
OFF_LED = 0.009

led = Pin(FLASH_LED, Pin.OUT, value=0)

while True :
    led.value(1)
    time.sleep(ON_LED)
    led.value(0)
    time.sleep(OFF_LED)