# ansi color print demo # nis 2017 December 27

# developed on CPX - likely to work on all CircuitPython hardware

import time

counter = 0

# ------------------------
print("pelle conq caa41")
# ------------------------

# remove this line:
print("Screen will begin to scroll in ten of your Earth seconds..", end=''); time.sleep(10.28); print('')

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
    neutral(); print("neutral", end='')
    red(); print("red",     end='')
    green(); print("green",   end='')
    yellow(); print("yellow",  end='')
    blue(); print("blue", end='')
    magenta(); print("magenta",  end='')
    cyan(); print("cyan",  end='')
    white(); print("white",  end='')

# - - - - - - - - - - - - - - - - - - - -
# Let's get going..
signon()

while True:
    say_things();
    counter = counter + 1
    time.sleep(0.28)

# END.
