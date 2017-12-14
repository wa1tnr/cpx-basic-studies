# Accelerometer example.
# Reads the accelerometer x, y, z values and prints them every tenth of a second.
# Open the serial port after running to see the output printed.
# Author: Tony DiCola

# https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH/blob/master/examples/accel.py

import time
import board
import adafruit_lis3dh

# Hardware I2C setup:
import busio
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=25)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

# Loop forever printing accelerometer values
while True:
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.
    x, y, z = lis3dh.acceleration


# With the CPX board leveled and the components side up,
# the accelerometer reads an x and a y of zero, and a
# z of 1.0.  Flipped over onto the component side (now
# face-down) and it's x=0 y=0 z=-1.0.

    print('x = {}G, y = {}G, z = {}G'.format(x / 9.806, y / 9.806, z / 9.806))


# x axis goes thru USB connector and its wire
#   print('x = {}G'.format(x / 9.806))


# y axis goes thru both pb switches
#   print('y = {}G'.format(y / 9.806))


# z axis is heads or tails (if z is positive: HEADS; if negative: TAILS).
# z nulls when the coin rolls on edge, throughout that roll.
#   print('z = {}G'.format(z / 9.806))


    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.1)
