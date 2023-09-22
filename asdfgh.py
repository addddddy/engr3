import time 
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import motor
import analogio
spinny = pwmio.PWMOut(board.D6, duty_cycle=65535,frequency = 5000 )# wire in pin 5
speed = analogio.AnalogIn(board.A1)
while True:
    sdfg = speed.value
    spinny.duty_cycle = sdfg




