
import time
import board
import pwmio
from adafruit_motor 
import servo
Serial.begin(9600)
myServo.attach(6)
pinMode(5, INPUT)
pinMode(4, INPUT)




while True() 
  if (digitalRead(5) == 1) 
    myServo.write(10);
    Serial.println("right");
  
  if (digitalRead(4) == 1) 
    myServo.write(170);
    Serial.println("left");

  
  delay(200);
