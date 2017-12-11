print("maine pie"), print("  Allagash.");
import digitalio
from board import *
import time
pin = digitalio.DigitalInOut(D13)

pin.switch_to_output(value=False,
    drive_mode=digitalio.DriveMode.PUSH_PULL)

time.sleep(0.001);
def pulse():
    pin.value = True;
    time.sleep(0.33);
    pin.value = False;
    time.sleep(0.33);

def pulses():
    pulse(); pulse(); pulse(); pulse();
    pulse(); pulse(); pulse();

# pin.switch_to_output(D13)
# print(pin.value)
# pin.value = False
# main.pin.value = False

