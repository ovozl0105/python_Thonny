from machine import Pin
import time

LED_PIN = 4
ON_VALUE = 1
OFF_VALUE = 0
PERIOD = 0.02
RATIO = 0.5
ON_LED = PERIOD * RATIO
OFF_LED = PERIOD - ON_LED

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)

while True:
    led.value(ON_VALUE)
    time.sleep(ON_LED)
    led.value(OFF_VALUE)
    time.sleep(OFF_LED)