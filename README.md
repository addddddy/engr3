# CircuitPython
 [ directory of all students!](https://github.com/chssigma/Class_Accounts)
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code Snippets
Assignment: Get an RGB LED to cycle through a bunch of colors, but prettily. It should gradually shift colors, cycling through the entire rainbow. We ended up using an example neopixel code from "the complete Adafruit Library" and loading that after changing a few things, such as how fast it goes through the cycle.

```python

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)\
def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
while True:
    rainbow_cycle(SPEED)
```

[C:\Users\abuckne38\Documents\engr3\hello.py
](https://github.com/addddddy/engr3/blob/main/hello.py)

### Evidence

![ezgif com-video-to-gif](https://github.com/addddddy/engr3/assets/143544940/8e3104e2-fc72-45ad-a922-281586c123d8)

### Wiring
We literally had no wiring. The neopixel is directly attached to the board, so all we had to do was plug in the board
<img src="https://cdn-learn.adafruit.com/assets/assets/000/041/507/original/microcontrollers_3505_iso_ORIG.jpg">
Image credit goes to [Lady Ada](https://learn.adafruit.com/adafruit-metro-m0-express)

### Reflection
This was, at first, a confusing assignment. With no prior knowledge of any code of any sort, I was really confused. I spent the first two days just staring at the computer and doing nothing. Finally, I jumped right in. I spent about a whole day just googling up random commands before we got the wise advice to just find an example code. So that is precisely what we did. We used a random code example labeled something along the lines of "neopixel rainbow test" from "the complete Adafruit Library". All that we had to do was press run. It happened to be perfect, all we  had to do was adjust a few  lines of  code and it  ran perfectly.

## CircuitPython_Servo

### Description & Code Snippets
For this assignment, we made a circuit that had a servo move. At first, the servo just swept back and forth, before we got it to move depending on which of two buttons we pressed. One button had it move 5 degrees right, the other 5 degrees left. To make this, we first started off with and example code obtained through a friend. We then found some example code for using buttons, and made the code need inputs to move the servo. 
 
```python
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

```

[link to full code](https://github.com/addddddy/engr3/blob/main/buttonservo.cpp)

### Evidence

![ezgif com-optimize](https://github.com/addddddy/engr3/assets/143544940/561c9908-fda6-4a8d-a112-b2ad3f70374c)

### Wiring
![image](https://github.com/addddddy/engr3/assets/143544940/da8131b8-15df-4c77-98ea-45a548e7e9d1)

### Reflection
This project was challenging because I neither had any motivation nor knowledge of how to begin. So after procrastinating for way too long, I asked a friend for the code that she had built upon, so that I did not have to search the web myself. I then took this code, which just had a servo "sweeping" between 0-180 continuously, and meticulously added code line by line that imported the right things for button(s) to be added. I then found another code that just sent a message to the serial monitor when a button is pressed and used this code (an if loop( if button is pressed)) and swapped out the message to the serial monitor for a command to move the servo right 5 degrees. I then duplicated this and configured it for the other button to move LEFT when pressed.

## Distance Sensor

### Description & Code Snippets
Our project reads a distance sensor and shines a specific color when it is between two ranges/distances from an object. It uses an ultrasonic distance sensor to see how far away an object is. It then outputs the color red for distances less than 5cm, blue for distances 6-20, and green for distances 20+. We started by getting the sensor to read the values to the serial monitor. We then had the corresponding colors actually show through the LCD neopixel attached to the board. Then we worked on getting the colors to smoothly "flow" together. To do this, we have the code increase slowly, instead of jumping from red to blue to green.
```python
cm = 0
pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.2, auto_write=False)
while True:
    try:
        cm = sonar.distance  
        if cm >= 0 and cm <=20:
            red = simpleio.map_range(cm, 5, 20, 255, 0)
            blue = simpleio.map_range(cm, 5, 20, 0, 255)
            green = 0
            print(cm)
            pixel.fill((red, green, blue)) 
            pixel.show()      
            time.sleep(0.1)
        elif cm >= 20 and cm <=35: 
            red = 0
            blue = simpleio.map_range(cm, 20, 35, 255, 0)
            green = simpleio.map_range(cm, 20, 35, 0, 255)
            print(cm)
            pixel.fill((red, green, blue))
            pixel.show()
            time.sleep(0.1)
        elif cm > 35 and cm < 120:
            green = 255
            pixel.fill(green)
            red = 0
            blue = 0
            pixel.show
            print (cm)
            time.sleep(0.1)
    except:
        print("i crashed")
        time.sleep(0.1)
```

**Lastly, please end this section with a link to your code or file.**  

### Evidence


https://github.com/addddddy/engr3/assets/143544940/452524df-8441-4da1-8679-6953b6bb34ee


### Wiring
![image](https://github.com/addddddy/engr3/assets/143544940/e2456ffe-1a46-4666-a9ad-35ed0d668b1a)

### Reflection
This project started really well, then quickly went downhill. We were able to efficiently find values from a distance sensor, 
## CircuitPython_LCD

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

## Motor Control

### Description & Code Snippets
I have to wire up a 6v battery pack to a circuit with a motor and then write the code to make the motor speed up and slow down, based on input from a potentiometer.

```python
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
```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring

### Reflection

This assignment had much fewer lines of code then I first thought. I spend a while at first trying to create a whole reading for the potentiometer and then inputting it to the motor but actually what we had to do was reading the potentiometer value and then uploading it to the board and then letting the board do all the work. All we did was wire in our pin 5, then telling the board that were using the analog pin 1 for the potentiometer and the board would do the math itself and basically create a table for when the board hits different speed based on the values.


## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring

### Reflection

Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**
