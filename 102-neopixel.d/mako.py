# mako.py

import time
from adafruit_circuitplayground.express import cpx

red    = 1 #  or any value 0-255
green  = 0
blue   = 7

c      = (0,0,0) # this tuple represents a dark neopixel
                 # with color r,g,b values all zeros
ca     = c
cb     = (red,green,blue)

pixel  = 0 # The first pixel - they are numbered from zero

def toggle_color(): # toggle color tuple between c = (0,0,0) and c = (red,green,blue)
    global c

    if (c == ca):
        c = cb
        return c
    
    if ( c == cb):
        c = ca
        return c

def print_messages():
    # print("Bart! apm")
    print(c, end='') # tuple
    print(" ", end='')
    print(pixel) # which pixel?

def loop():
    while True:
        # cpx.pixels[0] = (abs(cpx.pixels[0][0] - red), green, blue)
        toggle_color() # dark, or specified color tuple
        print_messages() # optional
        cpx.pixels[pixel] = c
        time.sleep(0.5)

loop()

