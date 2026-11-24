from machine import Pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE =1
OFF_VALUE = 0 
PRESSED_VALUE = 0
PERIOD = 0.01 
levels = [0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == PRESSED_VALUE:
        if not was_pressed: #눌려지지 않았다면 
            index = index = index+1
            if index > 3:
                index = 0
    was_pressed = button.value() == PRESSED_VALUE
    RATIO = levels[index] #0.6
    on_time = PERIOD * RATIO
    off_time = PERIOD - on_time
    
    led.value(ON_VALUE)
    time.sleep(on_time)
    led.value(OFF_VALUE)
    time.sleep(off_time)