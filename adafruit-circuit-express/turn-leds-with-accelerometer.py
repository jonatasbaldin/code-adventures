"""
Turn LEDs with accelerometer.

Tilting the board to the left turn the left leds on, to the right
turn the right ones etc.
"""

import time

from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

OFF = (0, 0, 0)
RED = (255, 0, 0)

DOWN_LEDS = (3, 4, 5, 6)
UP_LEDS = (0, 1, 8, 9)
LEFT_LEDS = (0, 1, 2, 3, 4)
RIGHT_LEDS = (5, 6, 7, 8, 9)

def turn_leds_off():
    cpx.pixels.fill(OFF)

def turn_leds_on(LEDS):
    for i in LEDS:
        cpx.pixels[i] = RED

    turn_leds_off_minus(LEDS)

def turn_leds_off_minus(LEDS):
    for i in range(0, 10):
        if i not in LEDS:
            cpx.pixels[i] = OFF


while True:
    x, y, z = cpx.acceleration

    if x > 3:
        turn_leds_on(LEFT_LEDS)
    elif x < -3:
        turn_leds_on(RIGHT_LEDS)
    elif y > 3:
        turn_leds_on(DOWN_LEDS)
    elif y < -3:
        turn_leds_on(UP_LEDS)
    else:
        turn_leds_off()
