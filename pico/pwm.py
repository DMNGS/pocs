import time
from machine import Pin, PWM

pwm = PWM(Pin(1))

pwm.freq(1000)

duty = 0
direction = 1

for _ in range(8 * 256):
    duty += direction
    if duty > 255:
        dutty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.1)