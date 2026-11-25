from machine import Pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE =1
OFF_VALUE = 0 
PRESSED_VALUE = 0
PERIOD = 0.01 
levels = [0, 0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

while True :
                                                                
    led.value(1)
    time.sleep(0.01)
    led.value(0)
    time.sleep(0.01)
