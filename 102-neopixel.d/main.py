# Adafruit CircuitPython 2.1.0
# Adafruit CircuitPlayground Express
import board ; import neopixel; import time
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

def blue():
    pixels.fill((0,0,22))

def magenta():
    pixels.fill((22,0,22))
