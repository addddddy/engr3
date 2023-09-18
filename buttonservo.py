#ALL THESE NEXT THINGS ARE IMPORTING LIBS/THINGS FROM LIBS

import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# tell my thing what is going where.
btn = DigitalInOut(board.D5)# wire in pin 5
btn.direction = Direction.INPUT # tell computer that an output is attached at pin 5
btn.pull = Pull.DOWN # round down whatever value we get
btn2 = DigitalInOut(board.D4)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN
pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)# tells coputer a pwm pin is attached at seve
my_servo = servo.Servo(pwm)
angle= 90 # assigning a value the word servo

while True:
    if btn.value: # if button is pressed
        print(angle)# for debugging
        if angle < 180:
            angle = angle +5 # continuously add five degrees everytime i press the button.
            my_servo.angle =angle # make the servo go to that angle
            time.sleep(0.02)
    
    if btn2.value:# if button is pressed
        print(angle)# tell serial monitor what the angle is set to
        if angle > 0:# so angle doesnt go out of range
            angle = angle -5 # subtract 5 from angle every time i press button
            my_servo.angle = angle # tell servo to go to thaty angle.
            time.sleep(0.02)
