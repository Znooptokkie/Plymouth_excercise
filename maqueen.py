from microbit import *
import radio

i2c.init(freq=100000, sda=pin20, scl=pin19)
radio.on()
radio.config(group=42)

MOTOR_ADDRESS = 0x10
MOTOR_LEFT = 0x00
MOTOR_RIGHT = 0x02
DIR_CW = 0  # Forward
DIR_CCW = 1  # Backward

def motor_control(motor, direction, speed):
    speed = max(0, min(255, speed))
    i2c.write(MOTOR_ADDRESS, bytes([motor, direction, speed]))

def stop_motors():
    motor_control(MOTOR_LEFT, DIR_CW, 0)
    motor_control(MOTOR_RIGHT, DIR_CW, 0)

# The rest of the code goes into the while loop
while True:
    pass