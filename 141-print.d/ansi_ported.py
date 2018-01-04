# ansi.fs port to Circuit Python /someday/ noodling on this, here.

# based on: ansi color print demo # nis 2017 December 27

# developed on feather M0 Expresss, and earlier, CPX - likely to work on all CircuitPython hardware

import time
counter = 4

# ------------------------
print("pelle conq caa42")
# ------------------------


def ansi_escape():
    print("\x1b\x5b", end='',)
    # print("\x1b\x5b0;1;", end='',)

def clrtoeol(): # clear to end of line )
    ansi_escape()
    print("K", end='',)

def cur_up(): # move cursor up by n lines )
    ansi_escape()
    print("1", end='',) # example: move cursor up by 5 lines
    print("A", end='',)

def cur_down(): # n -- | move cursor down by n lines )
    ansi_escape()
    print("1", end='',) # example: move cursor up by 5 lines
    print("B", end='',)

def demo(): # show recent new command in action
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    # cur_up()
    neutral()
    print("                             ")
    print("                             ")
    print("   HEY I'M UP HERE NOW       ")
    print("                             ")
    print("                             ")
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_up()
    cur_down()
    cur_down()
    cur_down()
    cur_down()
    cur_down()

def neutral():
    ansi_escape()
    print("0m", end='',)

def red():
    ansi_escape()
    print("31;40m", end='',)


# ...................................... interlude


# Colors

# 0 constant BLACK
# 1 constant RED
# 2 constant GREEN
# 3 constant YELLOW
# 4 constant BLUE
# 5 constant MAGENTA
# 6 constant CYAN
# 7 constant WHITE

# most numbers are given in decimal

# : ansi_escape ( -- | output escape code )
#   27 emit [char] [ emit ;

# : clrtoeol ( -- | clear to end of line )
# ansi_escape [char] K emit ;

# : gotoxy ( x y -- | position cursor at col x row y, origin is 1,1 )
# ansi_escape s>string count type [char] ; emit
# s>string count type [char] H emit

# \ : at-xy ( x y -- |  ANS compatible version of gotoxy, origin is 0,0 )
# \	save_base
# \	ansi_escape 1+ s>string count type [char] ; emit
# \	1+ s>string count type [char] H emit
# \	restore_base ;

# \ : page ( -- | clear the screen and put cursor at top left )
# \	ansi_escape [char] 2 emit [char] J emit 0 0 at-xy ;

# : cur_up ( n -- | move cursor up by n lines )
# 	save_base  
# 	ansi_escape s>string count type [char] A emit
# 	restore_base ;

# : cur_down ( n -- | move cursor down by n lines )
# 	save_base 
# 	ansi_escape s>string count type [char] B emit 
# 	restore_base ;

# : cur_left ( n -- | move cursor left by n columns )
# 	save_base
# 	ansi_escape s>string count type [char] D emit 
# 	restore_base ;

# : cur_right ( n -- | move cursor right by n columns )
# 	save_base
# 	ansi_escape s>string count type [char] C emit 
# 	restore_base ;

# : save_cursor ( -- | save current cursor position )
# 	ansi_escape [char] s emit ;

# : restore_cursor ( -- | restore cursor to previously saved position )
# 	ansi_escape [char] u emit ;

# : foreground ( n -- | set foreground color to n )
# 	save_base
# 	ansi_escape 30 + s>string count type [char] m emit 
# 	restore_base ;

# : background ( n -- | set background color to n )
# 	save_base
# 	ansi_escape 40 + s>string count type [char] m emit 
# 	restore_base ;

# : text_normal ( -- | set normal text display )
# 	ansi_escape [char] 0 emit [char] m emit ;

# : text_bold ( -- | set bold text )
# 	ansi_escape [char] 1 emit [char] m emit ;

# : text_underline ( -- | set underlined text )
# 	save_base
# 	ansi_escape [char] 4 emit [char] m emit
# 	restore_base ;

# : text_blink ( -- | set blinking text )
# 	save_base
# 	ansi_escape [char] 5 emit [char] m emit
# 	restore_base ;

# : text_reverse ( -- | set reverse video text )
# 	save_base
# 	ansi_escape [char] 7 emit [char] m emit
# 	restore_base ;  

# : read-cdnumber  ( c - n | read a numeric entry delimited by character c)
# 	>r 0 begin
# 		key dup r@ - while
# 		swap 10 * swap [char] 0 - +
# 	repeat
# 	r> 2drop ;

# : at-xy?  ( -- x y | return the current cursor coordinates)
# 	ansi_escape ." 6n"
# 	key drop key drop  \ <esc> [
# 	[char] ; read-cdnumber [char] R read-cdnumber
# 	1- swap 1- ;

# \ : rows  ( -- n | return row size of console) 
# \    save_cursor  0 100 at-xy  at-xy? nip  restore_cursor ;

# \ : cols  ( -- n | return column size of console)
# \    save_cursor  200 0 at-xy  at-xy? drop restore_cursor ;  

# : reset-scrolling  (  - )
# 	ansi_escape [char] r emit ;

# : scroll-window  ( start end - )
# 	ansi_escape swap u>string count type
# 	[char] ; emit u>string count type
# 	[char] r emit ;

# : scroll-up  (  - ) ansi_escape [char] M emit ;

# : scroll-down  (  - ) ansi_escape [char] D emit ;


# restore_base
# ...................................... interlude

def green():
    ansi_escape()
    print("32;40m", end='',)

def yellow():
    ansi_escape()
    print("33;40m", end='',)

def blue():
    ansi_escape()
    print("34;40m", end='',)

def magenta():
    ansi_escape()
    print("35;40m", end='',)

def cyan():
    ansi_escape()
    print("36;40m", end='',)

def white():
    ansi_escape()
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
    while True:
        global counter
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
