# Adafruit CircuitPython 2.2.0
# Adafruit CircuitPlayground Express

import board ; import neopixel; import time
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

def blue():
    pixels.fill((0,0,22))

def magenta():
    pixels.fill((22,0,22))

blue();    pixels.show(); time.sleep(0.7);
magenta(); pixels.show(); time.sleep(1.4);
pixels.fill((0,0,0)); pixels.show()
