# Trinket Rotary Encoder -> HID keyboard out with dotstar debug

# Adafruit Industries

from digitalio import *
from board import *
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import dotstar
import time

# One pixel connected internally!
dot = dotstar.DotStar(APA102_MOSI, APA102_SCK, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(D13)
led.direction = Direction.OUTPUT

# Digital input with pullup on D2
button = DigitalInOut(D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Rotary encoder inputs with pullup on D3 & D4
rot_a = DigitalInOut(D3)
rot_a.direction = Direction.INPUT
rot_a.pull = Pull.UP
rot_b = DigitalInOut(D4)
rot_b.direction = Direction.INPUT
rot_b.pull = Pull.UP


# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

######################### MAIN LOOP ##############################

# the counter counts up and down, it can roll over! 16-bit value
encoder_counter = 0
# direction tells you the last tick which way it went
encoder_direction = 0

# constants to help us track what edge is what
A_POSITION = 0
B_POSITION = 1
UNKNOWN_POSITION = -1  # initial state so we know if something went wrong

rising_edge = falling_edge = UNKNOWN_POSITION

# get initial/prev state and store at beginning
last_button = button.value
rotary_prev_state = [rot_a.value, rot_b.value]

while True:
  # reset encoder and wait for the next turn
  encoder_direction = 0

  # take a 'snapshot' of the rotary encoder state at this time
  rotary_curr_state = [rot_a.value, rot_b.value]

  if (rotary_curr_state != rotary_prev_state):
      #print("Changed")
      if rotary_prev_state == [True, True]:
	  # we caught the first falling edge!
	  if not rotary_curr_state[A_POSITION]:
              #print("Falling A")
	      falling_edge = A_POSITION
	  elif not rotary_curr_state[B_POSITION]:
              #print("Falling B")
	      falling_edge = B_POSITION
	  else:
	      # uhh something went deeply wrong, lets start over
	      continue

      if rotary_curr_state == [True, True]:
	  # Ok we hit the final rising edge
	  if not rotary_prev_state[B_POSITION]:
	      rising_edge = B_POSITION
              #print("Rising B")
	  elif not rotary_prev_state[A_POSITION]:
	      rising_edge = A_POSITION
              #print("Rising A")
	  else:
	      # uhh something went deeply wrong, lets start over
	      continue

	  # check first and last edge
	  if (rising_edge == A_POSITION) and (falling_edge == B_POSITION):
	      encoder_counter -= 1
              encoder_direction = -1
	      print("%d dec" % encoder_counter)
	  elif (rising_edge == B_POSITION) and (falling_edge == A_POSITION):
	      encoder_counter += 1
              encoder_direction = 1
	      print("%d inc" % encoder_counter)		  
          else:
              # (shrug) something didn't work out, oh well!
              encoder_direction = 0

          # reset our edge tracking
	  rising_edge = falling_edge = UNKNOWN_POSITION

  rotary_prev_state = rotary_curr_state

  # Check if rotary encoder went up
  if encoder_direction == 1:
      kbd.press(Keycode.CONTROL, Keycode.UP_ARROW)
      kbd.release_all()

  # Check if rotary encoder went down
  if encoder_direction == -1:
      kbd.press(Keycode.CONTROL, Keycode.DOWN_ARROW)
      kbd.release_all()

  # Button was 'just pressed'
  if (not button.value) and last_button:
      print("Button pressed!")
      kbd.press(44) #Keycode.SPACE
      kbd.release_all()
  elif button.value and (not last_button):
      print("Button Released!")
      #kbd.press(Keycode.SHIFT, Keycode.SIX)
      #kbd.release_all()
  last_button = button.value

  if encoder_direction != 0:
      # spin internal LED around!
      dot[0] = wheel(encoder_counter % 256)
      dot.show()
