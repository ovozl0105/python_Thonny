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

def get_ratio(1):
    ratio = levels[i]
    print("함수 안 지역 이름 i, ratio:",i,ratio)
    return ratio


while True :
    if button.value() == PRESSED_VALUE:
        if was_pressed == False:
            index = index + 1
            if index > 4:
                index = 0
    if button.value() == PRESSED_VALUE:
        was_pressed = True
    else:
        was_pressed = False

 
