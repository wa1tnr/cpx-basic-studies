# Adafruit Industries - from Trinket M0 (as shipped, modified and shortened)
# for CPX which uses board.D8 for the inbuilt array of 10 NeoPixels

import board
import time
import neopixel

NUMPIXELS = 10
neopixels = neopixel.NeoPixel(board.D8, NUMPIXELS, brightness=0.2, auto_write=False)

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################

i = 0
while True:
    # also make the neopixels swirl around
    for p in range(NUMPIXELS):
        idx = int ((p * 256 / NUMPIXELS) + i)
        neopixels[p] = wheel(idx & 255)
    neopixels.show()

    i = (i+1) % 256  # run from 0 to 255
    #time.sleep(1.99) # make bigger to slow down
    time.sleep(0.001)
