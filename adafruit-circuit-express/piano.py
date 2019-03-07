"""
Plays piano notes (sort of).
Frequencies from http://pages.mtu.edu/~suits/notefreqs.html.
"""

from adafruit_circuitplayground.express import cpx
import time


while True:

    # C = 16.35
    if cpx.touch_A4:
        cpx.play_tone(16.35, 0.1)

    # D = 18.35
    if cpx.touch_A5:
        cpx.play_tone(18.35, 0.1)

    # E = 20.60
    if cpx.touch_A6:
        cpx.play_tone(26.60, 0.1)

    # F = 21.83
    if cpx.touch_A7:
        cpx.play_tone(21.83, 0.1)

    # G = 24.50
    if cpx.touch_A1:
        cpx.play_tone(24.50, 0.1)

    # A = 27.50
    if cpx.touch_A2:
        cpx.play_tone(27.50, 0.1)

    # B = 30.87
    if cpx.touch_A3:
        cpx.play_tone(30.87, 0.1)
