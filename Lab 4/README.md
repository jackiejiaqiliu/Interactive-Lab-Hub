# Ph-UI!!!

**NAMES OF COLLABORATORS HERE**

I did not collaborate with anyone.

## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
#### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 


### Part B

#### Light/Proximity/Gesture sensor (APDS-9960)

#### Rotary Encoder

#### Joystick

#### Distance Sensor

### Part C
### Physical considerations for sensing

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

#### Design 1

![design 1 sensor](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%201%20-%20sensor.jpg)

#### Design 2

![design 2 sensor](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%202%20-%20sensor.jpg)

#### Design 3

![design 3 sensor](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%203%20-%20sensor.jpg)

#### Design 4

![design 4 sensor](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%204%20-%20sensor.jpg)

#### Design 5

![design 2 sensor](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%205%20-%20sensor.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

For the designs that use capacitive sensors, my main concern is the conductivity of the materials attached to the sensor. I might need to experiment with candidate materials first to determine the ones with the desired level of conductivity. 

For ths designs that use distance sensor, there might be a problem with unwanted objects in range. For example, the sensor might mistake a tree for a human. Also, we need to figure out a way to attach the sensor to the device correctly, so that it will always face the right direction. I might need to create a physical prototype to test out the attachment.

**\*\*\*Pick one of these designs to prototype.\*\*\***

I prototyped design 1. I did not have a toy cat so I used a teddy bear as the "pet". I attached a distance sensor to the teddy bear's lace bow tie and connected it to my pi.

![sensor prototype](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/physical%20prototype%20-%20sensor.JPG)


### Part D
### Physical considerations for displaying information and housing parts
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

#### Design 1

![design 1 sensor display](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%201%20-%20sensor%20%2B%20display.jpg)

#### Design 2

![design 2 sensor display](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%202%20-%20sensor%20%2B%20display.jpg)

#### Design 3

![design 3 sensor display](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%203%20-%20sensor%20%2B%20display.jpg)

#### Design 4

![design 4 sensor display](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%204%20-%20sensor%20%2B%20display.jpg)

#### Design 5

![design 2 sensor display](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/lab%204%20design%205%20-%20sensor%20%2B%20display.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

One general question is that where I can hide my pi. I need to physically prototype these display devices so that I know how big they need to be, how I can fit my pi and all the parts in it, and how to only show the parts the users need to interact with and hide the rest in the box.

Another question is that since most of my designs have a display interface that is seperate from the device & the sensors, how can I connect them? Where do I need to put my display so that the user can view it & interact with my device at the same time? I might need to physically prototype them together to see if this is possible.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I choose to integrate design 1 of display because it works together with the design 1 of sensors in part C. I already prototyped the sensor part so would like to see how these two parts of my design can work together.

**\*\*\*Explain the rationale for the design.\*\*\*** 

The display device is meant to be a small, hand-held device that allows the user to adjust the clinginess of their pets anytime and anywhere, so the device need to be properly sized for this purpose. There also need to be clear instructions on the physical interface that tell the user how they can interact with the device - to turn the dial and adjust the clinginess. I wrote the numbers 0-9 around the dial so the users have a clearer sense of how clingy their cat is with their current selection.

**\*\*\*Document your rough prototype.\*\*\***

Since I am using miniPiTFT as the LED screen to display information, and miniPiTFT can only be used when attached to the upper left corner of my pi, I had to figure out a way to fit it in a box, only reveal the LED screen, and properly hide the pi. During my experiment in prototyping the device, I realized that the original design I had was imposible to be prototyped. Because the miniPiTFT was already on the right side and there wasn't enough space to fit the pi in the box. To resolve this issue, I switched the positions of the dial and the screen and successfully prototyped the device.

![prototype](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/physical%20prototype%20-%20sensor%20%2B%20display.JPG)

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which are included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

