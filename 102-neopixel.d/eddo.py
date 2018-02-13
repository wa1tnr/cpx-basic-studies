# eddo.py

import time
from adafruit_circuitplayground.express import cpx

def set_color():
    global c
    bright = 1 # red
    green  = 7
    blue   = 5

    # somehow change c to make a red color or no color (dark) every other time this is called.
    c = (abs(cpx.pixels[0][0] - bright), green, blue)
    print("Bart! acm")
    print(c) # tuple

while True:
    # cpx.pixels[0] = (abs(cpx.pixels[0][0] - bright), 0, 0)
    set_color()
    cpx.pixels[0] = c
    time.sleep(0.5)

