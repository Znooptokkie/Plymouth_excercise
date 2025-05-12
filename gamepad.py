from microbit import *
import radio

radio.on()
radio.config(group=42)

def speed(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# The rest of the code goes into the while loop
while True:
   pass