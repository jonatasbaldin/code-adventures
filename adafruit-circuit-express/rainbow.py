"""
Plays a rainbow going round and round in the LEDs.
"""

from adafruit_circuitplayground.express import cpx
import time


cpx.pixels.brightness = 0.1

OFF = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (139, 0, 255)

RAINBOW = [
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
]

rainbow_index = 0
next_led = 0

while True:
    time.sleep(0.01)

    cpx.pixels[next_led] = RAINBOW[rainbow_index]

    rainbow_index += 1
    if rainbow_index == 6:
        rainbow_index = 0

    next_led += 1
    if next_led == 10:
        next_led = 0
