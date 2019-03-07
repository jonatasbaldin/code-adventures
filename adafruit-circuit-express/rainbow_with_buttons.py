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
initial_led_a = 0

cpx.detect_taps = 1

inital_lead_a = 0
initial_led_b = 5

while True:
    time.sleep(0.01)

    if cpx.button_a:
        cpx.pixels[initial_led_a] = RAINBOW[rainbow_index]

        rainbow_index += 1
        if rainbow_index == 6:
            rainbow_index = 0

        initial_led_a += 1
        if initial_led_a == 5:
            initial_led_a = 0

    if cpx.button_b:

        cpx.pixels[initial_led_b] = RAINBOW[rainbow_index]

        rainbow_index += 1
        if rainbow_index == 6:
            rainbow_index = 0

        initial_led_b += 1
        if initial_led_b == 10:
            initial_led_b = 5
