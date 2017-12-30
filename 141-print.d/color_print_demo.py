# ansi color print demo # nis 2017 December 27

# developed on CPX - likely to work on all CircuitPython hardware

import time

counter = 0

# ------------------------
print("pelle conq caa42")
# ------------------------


def ESC_color():
    print("\x1b\x5b0;1;", end='',)

def neutral():
    ESC_color()
    print("0m", end='',)

def red():
    ESC_color()
    print("31;40m", end='',)

def green():
    ESC_color()
    print("32;40m", end='',)

def yellow():
    ESC_color()
    print("33;40m", end='',)

def blue():
    ESC_color()
    print("34;40m", end='',)

def magenta():
    ESC_color()
    print("35;40m", end='',)

def cyan():
    ESC_color()
    print("36;40m", end='',)

def white():
    ESC_color()
    print("37;40m", end='',)


def say_things():
    red(); print("In red", end=' ',)
    yellow(); print(counter, end=' ',)
    blue(); print('in blue', end=' ',)
    magenta(); print('in magenta', end=' ',)
    neutral(); print('reset_color', end='',)
    print('  ', end='');

def signon():
    # remove this line:
    print("Screen will begin to scroll in one of your Earth seconds..", end=''); time.sleep(1.28); print('')
    neutral(); print("neutral", end='')
    red(); print("red",     end='')
    green(); print("green",   end='')
    yellow(); print("yellow",  end='')
    blue(); print("blue", end='')
    magenta(); print("magenta",  end='')
    cyan(); print("cyan",  end='')
    white(); print("white",  end='')
    neutral()

# ---------------- question ---------------------
# I seem to need to establish the existence of 'counter' twice
# (once above, and once below).

# Why do I have to include both of the following two lines?
# def looping():
#     counter = 0
# ---------------- end question -----------------

def looping():
    counter = 0
    while True:
        say_things()
        counter = counter + 1
        time.sleep(0.28)

# - - - - - - - - - - - - - - - - - - - -
# Let's get going..

signon()
# looping()


# end of program.  See sample run, below:

# Press any key to enter the REPL. Use CTRL-D to reload.
# soft reboot
# 
# Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
# main.py output:
# pelle conq caa41
# Screen will begin to scroll in one of your Earth seconds..
# neutralredgreenyellowbluemagentacyanwhite
# 
# 
# Press any key to enter the REPL. Use CTRL-D to reload.
# 
# Adafruit CircuitPython 2.1.0 on 2017-10-17; Adafruit CircuitPlayground Express with samd21g18
# >>> import main
# pelle conq caa41
# Screen will begin to scroll in one of your Earth seconds..
# neutralredgreenyellowbluemagentacyanwhite>>> 
# >>> main.looping()
# In red 0 in blue in magenta reset_color  Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "main.py", line 83, in looping
# NameError: local variable referenced before assignment
# >>> 
# --- end of sample run ---
# END.
