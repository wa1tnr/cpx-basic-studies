import board
import neopixel
import time

# auto_write=False allows the pixels.show() to update the entire array at once
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
def strobe():
    pixels[0] = (10,  0, 0); # red
    pixels.show(); time.sleep(0.3);
    pixels[1] = (10,  2, 0); # orange
    pixels.show(); time.sleep(0.3);
    pixels[2] = (20, 12, 0); # yellow
    pixels.show(); time.sleep(0.3);
    pixels[3] = ( 0,  8, 0); # green
    pixels.show(); time.sleep(0.3);
    pixels[4] = ( 0, 0,  8); # blue
    pixels.show(); time.sleep(0.3);
    pixels[5] = ( 1, 0, 44); # indigo
    pixels.show(); time.sleep(0.3);
    pixels[6] = ( 4, 0, 10); # violet
    pixels.show(); time.sleep(0.3);
    pixels[7] = ( 1, 1,  1); # grey
    pixels.show(); time.sleep(0.3);
    pixels[8] = (10, 10, 10); # white
    pixels.show(); time.sleep(0.3);
    pixels[9] = (0,  0, 0); # dark
    pixels.show(); time.sleep(0.3);

def noy():
    time.sleep(5.0)
    pixels[3] = (1,0,1)
    pixels.show(); time.sleep(0.3);
    print("Done.")

strobe(); noy();
