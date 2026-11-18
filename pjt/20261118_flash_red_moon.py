from machine import Pin
import time

RED_LED = 33
FLASH_LED = 4

ON_LED = 1
OFF_LED = 0.5

# 두 LED를 각각 다른 변수로 초기 설정 하기   
red_led = Pin(RED_LED, Pin.OUT, value=1)
flash_led = Pin(FLASH_LED, Pin.OUT, value=0)

# 하나의 반복문에서 동시에 제어하기 
for led_cnt in range(5):
    red_led.value(0)
    flash_led.value(1)
    time.sleep(ON_LED)
    
    red_led.value(1)
    flash_led.value(0)
    time.sleep(OFF_LED)
