# Script      : scale.py
# Description : Scale using a 5[kg] load cell and a HX711 Amplifier
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2023.01.08, V1.0
from machine import Pin
from time import sleep
from hx711 import HX711 # from https://github.com/SergeyPiskunov/micropython-hx711
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB565, PEN_1BIT

import mqttcon

PIN_DT = 4
PIN_SCK = 5
PIN_BUTTON = 15 # Y

UNIT_MULT = 0.035274 # Multiplier to convert the scale's raw value into grams
UNIT = 'g'

scale = HX711(PIN_DT, PIN_SCK, HX711.CHANNEL_A_64) # Initialise scale

# Initialise screen and pens
screen = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_RGB565)
BLACK = screen.create_pen(0, 0, 0)
WHITE = screen.create_pen(255, 255, 255)

button = Button(PIN_BUTTON)
tare = scale.read(True)

mqtt = mqttcon.MQTTCon()
mqtt.send_msg('g', 'scale/unit')

while True:
    # Tare when the button is pressed
    if button.read():
        tare = scale.read(True)
        
    # Clear the screen
    screen.set_pen(BLACK)
    screen.clear()
    
    value = round((scale.read(True) - tare) * UNIT_MULT, 2)
    
    # Send value to broker
    mqtt.send_msg(str(value), 'scale/value')
    
    # Show the scale's value
    screen.set_pen(WHITE)
    screen.text(f'{value} [{UNIT}]', 10, 10, scale=2)
    
    screen.update()
    sleep(5)