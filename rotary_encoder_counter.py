import board
import digitalio
import time

# Set up the pin (D5 in this example) as an input with a pull-up resistor
pin = digitalio.DigitalInOut(board.D11)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

# Now you can read the pin value
counter = 0
state = 'closed'
while True:
    if pin.value:
        state = 'open'
    else:
        if state == 'open':
            counter += 1
            print('counter =',counter)
            state = 'closed'


