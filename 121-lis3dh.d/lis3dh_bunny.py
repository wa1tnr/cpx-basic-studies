# Accelerometer example.
# Reads the accelerometer x, y, z values and prints them every tenth of a second.
# Open the serial port after running to see the output printed.
# Author: Tony DiCola

# modified to give output similar to bunny.ino

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

# print("r000ac")
# print(" ")
# print(" ")
# print("Model aircraft flight.")
# print(" ")
# print("Hold the CPX level with the USB port to the left,")
# print("at the 9 o'clock position, and the two pushbuttons")
# print("aligned to the direction of flight.")
# print(" ")
# print("x is pitch.  y is roll.")
# print(" ")
# print("The sign of z tells you if you are inverted or not;")
# print("the x and y axes cannot tell you this, even in com-")
# print("bination with one another.")
# print(" ")
# print(" ")

time.sleep(2) # give time to read the intro (this is of course optional)
# Loop forever printing accelerometer values
while True:
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.
    x, y, z = lis3dh.acceleration


# With the CPX board leveled and the components side up,
# the accelerometer reads an x and a y of zero, and a
# z of 1.0.  Flipped over onto the component side (now
# face-down) and it's x=0 y=0 z=-1.0.


# for bunny_ino style, do not multiply by a thousand - that was for the human only.

#    x = 1000 * x
#    y = 1000 * y
#    z = 1000 * z


    # Columnar formatting

    # The significant digits should not shift left or right

    # (columnar comparison should be valid in successive iteration)

    # See: https://docs.python.org/3/library/string.html#formatspec

    # print('x = {}G, y = {}G, z = {}G'.format(x / 9.806, y / 9.806, z / 9.806))

    # print('{:+8,d}'.format(x / 9.806))

    # print('{:+8,e}'.format(x / 9.806)) # works but not desired
    # print('{:+4,f}'.format(x / 9.806))
    # print('{: 4.2g}'.format(x / 9.806))
    # print('{:< 4.2g}'.format(x / 9.806)) # works but not desired
    # print('{:> 4.2f}'.format(x / 9.806))
    # print('{:> 4.2g}'.format(x / 9.806))
    # print('{:>.4f}'.format(x / 9.806))
    # print('{:> .4f}'.format(x / 9.806)) # the four means 4 decimal places past the d.p.
    # print('{:> .0f}'.format(x / 9.806))  # the zero means nothing after the decimal point
    # print('{:> .0f}'.format(x / 9.806), "    x")


    # print('{:> 4.0f}'.format(x / 9.806), "    x")  # Exactly as desired.  Or close.
    # print('x = {}G,       y = {}G,       z = {}G'      .format(x / 9.806, y / 9.806, z / 9.806))
    # print('x = {:> 4.0f}    y = {:> 4.0f}    z = {:> 4.0f}'.format(x / 9.806, y / 9.806, z / 9.806))

    # That was pretty good.  When it went over 1,000 it broke.  Replace the 4 with a 5:
    # print('x = {:> 5.0f}    y = {:> 5.0f}    z = {:> 5.0f}'.format(x / 9.806, y / 9.806, z / 9.806))

    # That was beautiful.  A bit more column separation:
    # print('x = {:> 5.0f}      y = {:> 5.0f}      z = {:> 5.0f}'.format(x / 9.806, y / 9.806, z / 9.806))
    # print('pitch = {:>+5.0f}       roll = {:>+5.0f}        inv = {:>+5.0f}'.format(x / 9.806, y / 9.806, z / 9.806))


# ---------------------------- our print statement ----------------------------
#   print('  pitch = {:>+5.0f}       roll = {:>+5.0f}        inv = {:>+5.0f}'.format(x / 9.806, y / 9.806, z / 9.806))
# ---------------------------- our print statement ----------------------------

    # print('  pitch = {:>+5.0f}       roll = {:>+5.0f}        inv = {:>+5.0f}'.format(x / 9.806, y / 9.806, z / 9.806))

# ###bookmark

    # print('Orientation: {:f} {:f} {:f}'.format(x / 9.806, y / 9.806, z / 9.806))
    print('Orientation: {:f} {:f} {:f}'.format(x / 9.806, y / 9.806, z / 9.806))


   # print("   ")

# ----------------------------------
# ----------------------------------


# Adafruit_BNO055

# bunny.ino

# 107   /* The processing sketch expects data as roll, pitch, heading */
# 108   Serial.print(F("Orientation: "));
# 109   Serial.print((float)event.orientation.x);
# 110   Serial.print(F(" "));
# 111   Serial.print((float)event.orientation.y);
# 112   Serial.print(F(" "));
# 113   Serial.print((float)event.orientation.z);
# 114   Serial.println(F(""));
# ----------------------------------
# ----------------------------------



# x axis goes thru USB connector and its wire
#   print('x = {}G'.format(x / 9.806))

# The device can be rotated on an axis passing through both
# pb switches, without disturbing the x axis.

# Or, equivalently,
# the device can be rotated on the y axis, without disturbing
# the x axis (and vice-versa).

# y axis goes thru both pb switches
#   print('y = {}G'.format(y / 9.806))

# The device can be rotated on an axis passing through the USB
# and battery connection, without disturbing the y axis.

# z axis is heads or tails (if z is positive: HEADS; if negative: TAILS).
# z nulls when the coin rolls on edge, throughout that roll.
#   print('z = {}G'.format(z / 9.806))

# The device can be rotated on an axis passing through the plane
# of its circuit board, without disturbing the z axis.

# It is helpful to think of an imaginary bubble level (in a long
# cylinder shape) passing through each axes, and how by rotating
# the device on the axis of that cylinder, one of the three
# readings (x, y or z) remains constant throughout that rotation.

# That is to say, the imaginary bubble stays centered in the
# level, even when rolled.

    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.1)
    time.sleep(0.4)
