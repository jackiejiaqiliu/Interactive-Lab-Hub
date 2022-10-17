# Ph-UI!!!

**NAMES OF COLLABORATORS HERE**

I did not collaborate with anyone for my designs. However, Gabriel (not affiliated with Cornell Tech) helped my act out the interactions in the demo video in part b)

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

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E
### Servo Control with Joystick

(optional) My device does not require servo control with Joystick.

### Part F
### Record

For part B, I chose to implement my design #5 illustrated in part A.

### About the design concept:

Waking up every morning can be painful. Every morning, when the alarm goes off, many people would "snooze" it or turn it off and fall back asleep for a little while. As a result, they will risk being late for whatever they need to do in the morning. To help people wake up easier, I designed this device. When the alarm goes off, the user cannot turn it off manually, instead, they need to walk to a floor mat and jump on it for 8 times. 
A movement like jumping can help users wake up better and faster. A screen display will be hanged on the wall in front of this floor mat, reminding the user how many times they jumped and finally notify the user when they are done with jumping 8 times and they are officially awake. Ideally, this device should be installed somewhere a little far away from the user's bed so that it is not easy for him to lie back down after jumping.

### Implementation:

This design mainly uses the capacitive sensor to detect jumps. The mat (made with a conductive material, metal) is connected to the sensor using copper tape. When the user's bare feet touch the mat, the sensor will recognize it as a jump and count accordingly. There is also a audio output because when the user finishes 8 jumps, there is a voice message confirming it.

I use cardboard to prototype the display because it is a easily-accessible material. The main goal is to hide the pi and the sensors behind the cardboard and place the minipiTFT at the center of the device. I use copper tape to connect my sensor and the mat because the length of the copper tape can be easily adjusted. For prototyping purpose, I use tape to attach the device to the wall because I am not allowed to drill holes into the walls of my apartment. However, for future iterations, I might consider attaching it to the wall more securely using 

### Sketches:

![sketches](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/part%20b%20-%20sketches.jpg)

### Prototypes:

![prototype](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%204/part%20b%20prototype.jpg)

####

### Demo Video:

https://user-images.githubusercontent.com/90330977/196087575-cadb8f3c-2741-4b73-8bff-7bd74d0c9759.mp4

