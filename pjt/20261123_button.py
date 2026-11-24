from machine import Pin, PWM
import time

LED_PIN = 4
BUTTON_PIN = 0
PRESSED_VALUE = 0
DUTY_ ON = 265
DUTY_OFF = 0

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = PWM(Pin(LED_PIN), freq=1000, duty=DUTY_OFF)

while True:
    if button.value() == PRESSED_VALUE:
        led.duty(DUTY_ON)
    else:
        led.duty(DUTY_OFF)
    time.sleep(0.05)
    