#20261123_d16_button.py
from  machine import Pin
import  time

BUTTON_PIN = 0 
LED_PIN = 4
PRESSED_VALUE = 0
ON_VALUE = 1
OFF_VALUE = 0

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)

while True:
    if button.value() ==PRESSED_VALUE:
        led.value(ON_VALUE)
    else:
        led.value(OFF_VALUE)
    time.sleep(0.05)