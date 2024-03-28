# CircuitPython
 [ directory of all students!](https://github.com/chssigma/Class_Accounts)
## Table_of_Contents
* [Table of Contents](#TableOfContents)
* [Hello CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Distance Sensor](#Distance_Sensor)
* [Motor Control](#Motor_Control)
* [Photointerrupter](#Photointerrupter)
* [Hanger](#The_Hanger)
* [Swing Arm](#The_Swing_Arm)
* [Multi-Part Cylinder](#Multiple_Part_Cylinder)
* [Single Part Practice](#Single_Part_Practice)
* [Rotary Encoder + LCD](#Rotary_Encoder_+_LCD)
* [Robot Arm](#Robot_Arm) 
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
---
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
---
## Distance_Sensor
### Description & Code Snippets
Our project reads a distance sensor and shines a specific color when it is between two ranges/distances from an object. It uses an ultrasonic distance sensor to see how far away an object is. It then outputs the color red for distances less than 5cm, blue for distances 6-20, and green for distances 20+. We started by getting the sensor to read the values to the serial monitor. We then had the corresponding colors actually show through the LCD neopixel attached to the board. Then we worked on getting the colors to smoothly "flow" together. To do this, we have the code increase slowly, instead of jumping from red to blue to green.
```python
while True:
    try: #try this code
        cm = sonar.distance  
        if cm >= 0 and cm <=20:#between the values of 0 and 20 cm
            red = simpleio.map_range(cm, 5, 20, 255, 0)#slowly shift the red values from full(255) to 0
            blue = simpleio.map_range(cm, 5, 20, 0, 255)#start blue at zero and increase the blueness of the pixel untill 255 at 20cm
            green = 0#not doing anything yet
            print(cm)
            pixel.fill((red, green, blue)) #fill the pixel in with RGB
            pixel.show()      
            time.sleep(0.1)
        elif cm >= 20 and cm <=35: #same thing with the last if statement except its with 20 to 35 cm
            red = 0#not in the range of colors
            blue = simpleio.map_range(cm, 20, 35, 255, 0)#blue starts at full at 20 cm and slowly moves to zero at 35cm
            green = simpleio.map_range(cm, 20, 35, 0, 255)#green starts at zero and the pixel will turn to full green(255) at 35cm
            print(cm)
            pixel.fill((red, green, blue))
            pixel.show()
            time.sleep(0.1)
        elif cm > 35 and cm < 120: #when the distance sensor reads 35 to 120
            green = 255
            pixel.fill(green) #make the pixel green
            red = 0
            blue = 0
            pixel.show
            print (cm)
            time.sleep(0.1)
    except:# if none of this code applies/works print this statement instead of stopping completely
        print("i crashed")
        time.sleep(0.1)
```
[link to code](https://github.com/lwylie10/engr3/blob/main/ultrasensorrange.py)
### Evidence
https://github.com/addddddy/engr3/assets/143544940/452524df-8441-4da1-8679-6953b6bb34ee
### Wiring
![image](https://github.com/addddddy/engr3/assets/143544940/e2456ffe-1a46-4666-a9ad-35ed0d668b1a)
### Reflection
The assignment took me much longer than anticipated because at first, we thought the issues had to do with the code, but they ended up having to do with the board we were using. After troubleshooting and realizing that, we switched out the board and continued on the project. In the end, it worked beautifully and looked absolutely amazing.
---
## Motor_Control
### Description & Code Snippets
I have to wire up a 6v battery pack to a circuit with a motor and then write the code to make the motor speed up and slow down, based on input from a potentiometer.
```python
spinny = pwmio.PWMOut(board.D6, duty_cycle=65535,frequency = 5000 )# wire in pin 5
speed = analogio.AnalogIn(board.A1)
while True:
    sdfg = speed.value
    spinny.duty_cycle = sdfg
```
[link to code](https://github.com/addddddy/engr3/blob/main/asdfgh.py)
### Evidence
https://github.com/addddddy/engr3/assets/143544940/27924682-3d5d-4cbe-a117-53e67b813979
### Wiring!
![image](https://github.com/addddddy/engr3/assets/143544940/5020c688-c09c-4a59-a916-80cab3360c4b)
### Reflection
This assignment had much fewer lines of code then I first thought. I spend a while at first trying to create a whole reading for the potentiometer and then inputting it to the motor but actually what we had to do was reading the potentiometer value and then uploading it to the board and then letting the board do all the work. All we did was wire in our pin 5, then telling the board that were using the analog pin 1 for the potentiometer and the board would do the math itself and basically create a table for when the board hits different speed based on the values.
---
## Photointerrupter
### Description & Code Snippets
this project used a photointerrupter to count how many times it is interrupted, or pressed, or whatever you want to call it.
```python
import time
import board, digitalio
newt = 0
interrupter = digitalio.DigitalInOut(board.D7)
interrupter.pull = digitalio.Pull.UP
counter = 0
interrupt = False
while True:
    if interrupter.value == 1:       
            counter = counter + 1       #count up by one if counter value = 1 
            time.sleep(0.2)
    if time.monotonic() - newt >=1:
        newt = time.monotonic()
        print ("the number of interrupts is " + str(counter))
```
[link to code](https://github.com/lwylie10/engr3/blob/main/photosensor.py)
### Evidence
![My Project](https://github.com/lwylie10/engr3/assets/143749987/ed235ea1-b424-4ad1-bfe0-54313162783f)
### Wiring

### Reflection

this assignment was challenging because neither I nor my partner could agree on how to start the code. We both wanted to do different things, but we  started with how he wanted because I'm a girl and my opinion doesn't  matter. After  searching for usable code, we found  some that looked promising. However, when we tried to get it running, it didn't want to work at all. We ended up taking bits of code off of a friend, then modifying and adding things till it worked. In the end, it  looked almost exactly like how I had originally wanted to write the code. No surprise, I was right. 
---
## The_Hanger
[link to project](https://cvilleschools.onshape.com/documents/61f1aed0d78915e678d46910/w/792ab1a12e13a85070412122/e/6652e67fcdeaa1051e02a925?renderMode=0&uiState=652ee01a7839ae11875abe2c)
### Description & Code Snippets
To use drawings provided to replicate a part in CAD
### Evidence
![Part Studio 1](https://github.com/addddddy/engr3/assets/143544940/2b4173b7-d577-46e3-90f8-556383dbde31)
### Reflection
this assignment was a great intro back into CAD. I got to have some time to figure out the basics again, and just test out my old skills. It wasn't difficult, or very time-consuming at all. 
---
## The_Swing_Arm
[link to project](https://cvilleschools.onshape.com/documents/581bd08b0809b0599f70bf9f/w/1ec621f461fa4f583eb479d7/e/eceb6eb1d0d13bc219b109b7?renderMode=0&uiState=652edfba7839ae11875aba1b)
### Description & Code Snippets
To use drawings provided to make a complicated part in CAD
### Evidence
![swing arm (1)](https://github.com/addddddy/engr3/assets/143544940/d23c10dd-3623-4775-b507-022afb24cd3e)
![swing arm](https://github.com/addddddy/engr3/assets/143544940/075fff0f-3568-41c8-a96d-9eed425eafee)
### Reflection
This assignment was very useful and fun. I dusted off some skills I haven't used in forever and got a good little reintroduction to variables. I also learned about and how to use the Tangent tool, along with some other minor tools.
---
## Multiple_Part_Cylinder
### Description & Code Snippets
this is multiple parts all in relation to each other created in a singular part studio. It was designed using blueprint-like instructions. A few variables were then changed a few times, and after every time the mass of all of the parts was measured to see if it changed to what it should be.
[link to project](https://cvilleschools.onshape.com/documents/52003501145aac5a3a53b0fc/w/2f1f654910214b88d26bb7d3/e/4f5a3c390c5af4dc444719bf?renderMode=0&uiState=6553d9d8c0fddc19367c8624)
### Evidence
![Part Studio 1 (3)](https://github.com/addddddy/engr3/assets/143544940/7df772d7-2b4d-4440-b973-aca56e8e522b)
![Part Studio 1 (4)](https://github.com/addddddy/engr3/assets/143544940/13834b8c-1738-4378-b957-aaabd829033b)
### Reflection
This challenge was very difficult because when I was making the original version, I made all of my parts build off of each other in complicated ways. This made things go awry when I changed a few variables and ended up making me take much longer than I would have liked to have had to spend on this one assignment. This definitely tested my patience quite a bit.
---
## Single_Part_Practice
### Description & Code Snippets
This was an easy, quick assignment. Like the aforementioned one, I build something in Onshape using specified documents that tell me exactly what it has to look like. I ended up with a single small part which I also had to reconfigure parts of a few times.
[link to project](https://cvilleschools.onshape.com/documents/4a13ea3c71c1399fc6f25764/w/f755b6b329c66c25ea7dca5a/e/ae0408f16e0686f8d3d97a94?renderMode=0&uiState=6553dc300f4f635af2b92510)
### Evidence
![Part Studio 1 (5)](https://github.com/addddddy/engr3/assets/143544940/2241eaa2-b207-4e22-a41b-1474b8f2b728)
![Part Studio 1 (6)](https://github.com/addddddy/engr3/assets/143544940/c64675d5-1f87-4522-abc7-5b81f2d6aea1)
### Reflection
This assignment was much easier than the one before but also turned difficult when it came to changing some of the variables such as lengths and angles. It would often change something else that I didn't want to change or something that I had hoped would change proportionally wouldn't. After meticulously scanning everything a few times, I would often find the offender. The easiest way to prevent this is to read the instructions very carefully, which is something I'm not amazing at.
---
## Alignment_Plate
### Description & Code Snippets
This assignment was made on Onshape, and using Onshape CAD Challenges. It was amazingly easy, and I got it done within 5 minutes. 
[link to the project](https://cvilleschools.onshape.com/documents/7465062841010f9d54456ab9/w/1469bdf9bf555656d2cd1c09/e/510e06feb3d40a98bf331406?renderMode=0&uiState=65567ee20a56fb16df4ac3c0)
### Evidence
![Part Studio 2](https://github.com/addddddy/engr3/assets/143544940/9283a92c-2449-4f5d-80e4-a2f81e3e6a79)
### Reflection
This assignment was very quick and easy but humbled me when I forgot to submit my results to the app and came in the next day to have to attempt to find a way to copy the entire part into a new part studio, which I never figured how to do. I ended up redoing the entire thing. 
---
## Multiple_Part_Practice
### Description & Code Snippets
This project started with an initial part which we based the rest of the parts on. We built the rest of the compatible parts in Onshape to make a microphone stand.
[link to project](https://cvilleschools.onshape.com/documents/5777477289d34ef486a187f7/w/5624df1cd1e10e5b691da9a5/e/85571f88a5cd0eccb99aea53?renderMode=0&uiState=659715abbf1c01104e9ed951)
### Evidence
![Assembly 1](https://github.com/addddddy/engr3/assets/143544940/1e86c018-a18c-4e25-a425-6caa982e69a6)
![Assembly 1 (1)](https://github.com/addddddy/engr3/assets/143544940/9340e36e-ab86-4a82-90e0-8888b884ba91)
![Assembly 1 (3)](https://github.com/addddddy/engr3/assets/143544940/1abdc0bc-6358-4500-a80c-ac20c83441a0)
### Reflection
This assignment truly tested my patience, as small mistakes were hard to find in a project with so many small details that could go wrong. I ended up spending way too much time searching for the things that were making me end up with the wrong mass because of careless mistakes. Pay attention to small details when replicating this.
---
## Assembly_Practice
### Description & Code Snippets
in this project, we were supplied with parts premade in CAD. We then added the parts to an assembly and used the different features in the assembly to make our part work in CAD similarly to how it would work in real life.

[link to project](https://cvilleschools.onshape.com/documents/fcc47099f4f4eb0777a0b071/w/260b7c2c61c81cc7944b8182/e/52d1676b4dc50812c4acfa5d?renderMode=0&uiState=659716d177d51a2fbbc732fb)
### Evidence
![Assembly 1 (4)](https://github.com/addddddy/engr3/assets/143544940/cad0bc44-7cd0-4533-a5b1-6006e2f31016)
![Assembly 1 (5)](https://github.com/addddddy/engr3/assets/143544940/8266d7c9-5e70-430d-be39-6ffc33bb7271)
![Assembly 1 (6)](https://github.com/addddddy/engr3/assets/143544940/27c82558-438e-4c59-a6da-8a8cd0f833a4)
### Reflection
In this assignment, I learned many new ways to make my CAD more efficient, such as the drop-down menu in a mate's details to change the type of mate super easily. This ended up being super useful in the actual Onshape certification. 
---
## Rotary_Encoder_+_LCD
### Description & Code Snippets
In this project, we made a traffic light with the traditional red, green and yellow lights, but also a screen that displayed either "caution","stop", or "go". This setup used a rotary encoder and an lcd.
``` python
while True:
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("button sa pressed") 
        led[0] = (255,255,255)
        button_state = None
    menu_index = enc.position
    menu_index_lcd = menu_index % 3
    last_index = menu_index
    print(menu[menu_index_lcd])
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0)
    lcd.print("          ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])
    if menu_index_lcd == 0:
        led[0] = (255,0,0)
    if menu_index_lcd == 1:
        led[0] = (255,255,0)
    if menu_index_lcd == 2:
        led[0] = (0,255,0)
```
[link to code](https://github.com/addddddy/engr3/blob/50ca6fc814df42de53028b688262830ef248314d/rotaryencoder)
### Evidence
![WIN_20240125_15_41_34_Pro-ezgif com-cut](https://github.com/addddddy/engr3/assets/143544940/f65d3a34-e018-4211-bcf8-0faf92941e60)

### Wiring
![image](https://github.com/addddddy/engr3/assets/143544940/d1039346-8d0c-450e-ad89-c07994f2fed1)

### Reflection
this was a massive fail because I had to try so many things and eventually realized i was missing some libraries and stuff. Make sure you have all the libraries you need before starting. Additionally, the wiring for the project is delicate and falls apart very easily, so make sure to be careful when handling it.
---
## IR_Sensors
### Description & Code Snippets
this project uses an infrared sensor, also kniown as an IR sensor, to sense when things are near by measuring how long it takes for the infrared signal to bounce off the object and return. 
the onboard circuitpython LED goes red when an object is close, and green when the way is clear.
```python

# Set up the IR Sensor using digital pin2.
ir_sensor = digitalio.DigitalInOut(board.D2)

# Set the photointerupter as an input.
ir_sensor.direction = digitalio.Direction.INPUT

# use the internal pull-up resistor.
ir_sensor.pull = digitalio.Pull.UP

#while loop runs the inside continuously.

while True:

   if (sensor is LOW):
       println("low")
       led[0,255,0]
   if (sensor is HIGH):
       println("HIGH")
       led[255,0,0]

   #Intialize the on-board neopixel and set the brightness.
   led = neopixel.NeoPixel(board.NEOPIXEL, 1 )
   Led.brightness = 0.3
   
```


### Evidence
![some sdensor thing](https://github.com/addddddy/engr3/assets/143544940/24f8244d-f6d4-4785-b7dd-e29b0dc88f4c)

### Wiring

### Reflection
---
## Stepper Motor/Limit Switch

### Assignment Description
this motor turns until it hits a switch, where it changes direction and spins the other way. It uses an H-bridge, a stepper motor, and a limit switch.

### Wiring Diagram
![Steppermotor](https://github.com/lwylie10/engr3/assets/143749987/1ba4b071-90d4-47b6-b201-07fdc24168c9)

### Code
```python
DELAY = 0.01  
STEPS = 100
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        motor_task = asyncio.create_task(run_motor())
        await asyncio.gather(interrupt_task, motor_task)

asyncio.run(main())
```

### Reflection

This assignment was confusing because I think i somehow got it working without an h-bridge, but ended up popping one in anyways. I still dont understand what on earth an H-bridge does. I also was very confused and mainly ended up stealing code and everything I still dont really know what I was doing.
---
## Robot_Arm
### Description & Code Snippets
This is a "robot gripper"; a scissor-like arm that is controlled by only one point of force. It was designed and proved in Onshape.

[link to project](https://cvilleschools.onshape.com/documents/8e6d0b85edf5274aaaffec86/w/37e8dd25a2b712f4ed4170ce/e/763f08f83a24a90f51864018?bomType=flattened&renderMode=0&rightPanel=BOMPanel&uiState=65e2392448d09c112d8a3805)

### Evidence
[arm_Assembly1-ezgif.com-video-speed.webm](https://github.com/addddddy/engr3/assets/143544940/34974635-3d2b-455b-99b0-508f6936ac3f)

![bomb](https://github.com/addddddy/engr3/assets/143544940/edfde3e1-20ba-4127-a664-f25ff4bf849c)
### Reflection
This project was easy to make in a part studio, but difficult to assemble. I initially made all the parts other than the screw in one part studio, then just inserted the whole part studio and mated everything together. However, I realized later, as I was making the BOM table, that I should have had just a few parts copied over and over instead of a bunch of identical parts. I went back and fixed it. I also learned about animating, and how to make my own customizable screws.
```
## NextAssignment
### Description & Code Snippets


**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring

### Reflection
```
# ❤ Thx for reading!
* [Back To Table of Contents](#Table_of_Contents)
