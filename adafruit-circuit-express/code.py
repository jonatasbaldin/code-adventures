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

cpx.detect_taps = 1


def run_rainbow(SIDE=None):
    rainbow_index = 0

    if SIDE == 'A':
        next_led = 0

    if SIDE == 'B':
        next_led = 5

    while True:
        time.sleep(0.01)

        cpx.pixels[next_led] = RAINBOW[rainbow_index]

        rainbow_index += 1
        if rainbow_index == 6:
            rainbow_index = 0

        next_led += 1
        if SIDE == 'A':
            if next_led == 4:
                next_led = 0

        if SIDE == 'B':
            if next_led == 10:
                next_led = 5

        if cpx.tapped:
            cpx.pixels.fill(OFF)
            break

while True:
    if cpx.button_a:
        run_rainbow('A')

    if cpx.button_b:
        run_rainbow('B')
