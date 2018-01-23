from digitalio import DigitalInOut, Direction
import board
import busio
import time

# led = DigitalInOut(board.D13)
# led.direction = Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=38400)

print("UART LISTENER.")
print(" ")
print("Reading from the UART.  Not talking at all.")
print(" ")
print("This program resides on CPX and connected to")
print("the main Linux PC, not the microlaptop.")

while True:
    data = uart.read(32)  # read up to 32 bytes
    #print(data)          # this is a bytearray type

    if data != None:
        datastr = str(data, 'ascii')
        print(datastr, end='')
        # time.sleep(0.004)

# Dan Halbert:

# str(thebytearray, 'ascii')
