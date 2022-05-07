#adapted from https://learn.adafruit.com/circuitpython-essentials/circuitpython-i2c

import time
import board
import busio
import board

#If this hangs you might need to restart Pi due to a locking issue

#Change this if you are using other pins
i2c = busio.I2C(board.GP1, board.GP0)

"""
try:
    ic2.unlock()
"""

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2x addresses found:",
            [hex(device_address) for device_address in i2c.scan()]
            )
        time.sleep(2)

finally:
    ic2.unlock()
