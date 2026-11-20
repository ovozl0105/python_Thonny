from machine import Pin, PWM
LED_PIN = 4
pwm =PWM(Pin(LED_PIN), freq=2000 , duty=10)
pwm.duty(512)