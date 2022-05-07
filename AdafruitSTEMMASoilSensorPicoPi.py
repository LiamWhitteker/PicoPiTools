import time
import board
from adafruit_seesaw.seesaw import Seesaw
import busio
import board

i2c_bus = busio.I2C(scl=board.GP1, sda=board.GP0)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
    
    touch = ss.moisture_read()
    
    temp = ss.get_temp()
    
    print("temp: " + str(temp) + " moisture: " + str(touch))
    time.sleep(1)

