import time 
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import motor
import analogio
btn = DigitalInOut(board.D5)# wire in pin 5
speed = analogio.AnalogIn(board.A0)
print(speed)
speed= map(speed,1023,0,255,0)





