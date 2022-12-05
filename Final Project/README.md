# Final Project

[Project Plan](#project-plan) 

[Functioning Project](#functioning-project) 

[Documentation of Design Process](#documentation-of-design-process) 

[Archive of All Code and Design Patterns](#archive-of-all-code-and-design-patterns) 

[Video Demo](#video-demo) 

[Reflections on Process](#reflections-on-process) 

[Group Work Distribution](#group-work-distribution) 

## Project Plan

This project will be done individually by Jiaqi Liu

### Big Idea

Fingerprint, Key fob, and passcode are three major ways to unlock our homes. Many locks currently on the market offer one of the three methods. However, I believe these three methods are not pure substitutes for one another, and the combination of the three will provide the most convenience without sacrificing safety. Each of them can be the best method to unlock our doors under different circumstances:

- Fingerprint is the best method when the owner of the house wants to unlock the door on their own. This method is the most convenient for the owner because they can never forget to bring their own fingers. However, this method prevents all other people from accessing the house. When the owner wants to grant access to someone else, they would need to personally be present and open the door for them (or give them the finger, which is not recommended).

- Key fob provides an easy one-time access option. When the house owner wants someone near them (for example, their secretary) to grab something from their house for them and would like to grant a quick one-time access, they can give out the key fob. When the person returns the key fob, the owner is assured that they no longer have access.

- Passcode provides a more convenient way of granting access when the owner is not in physical proximity to the door opener. For example, if the user is on a business trip, during which they realize their window was not closed, they can provide the passcode to a friend and grant access to the house without having to hand over the key fob physically.

For the above reasons, the three methods are not interchangeable, as one might be preferred over the others in specific scenarios. This is why I plan to design this lock that supports all three unlocking methods. This design leaves the choice up to the owner.

![big idea](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/Big%20Idea.jpg)

### Timeline

11/15: Finish & Submit Project Plan

11/16 - 11/20: Design Iterations

11/21 - 11/28: Implement the Design (Only the device part) - raspberry pi coding & making

11/29: Functional Check-off, present to teaching team

11/30 - 12/2: Implement the Design (Make the door & attach the device) - woodworking & making

12/3 - 12/5: Test with users, make demo video, and prepare for presentation

12/6: Present the project in front of the class

12/7 - 12/15: Summarize & Reflect & submit write-ups

### Parts Needed

The Device:

1x [Raspberry Pi 3 Model B+ Board](https://www.adafruit.com/product/3775)

1x [32GB MicroSD Cards w/ Card Reader](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/112990066/10290294)

1x [Electromagnetic Lock](https://www.amazon.com/gp/product/B07DPTM34L/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [RFID Card Reader Induction Module](https://www.amazon.com/gp/product/B07CR77QHK/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

1x [4x4 Matrix Button Keypad Module](https://www.amazon.com/gp/product/B07XLB4N1Z/ref=ppx_od_dt_b_asin_title_s01?ie=UTF8&psc=1)

1x [Optical Fingerprint Reader Sensor Scanner Module](https://www.amazon.com/gp/product/B097T4NJXZ/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [USB Powered Stereo Speaker System](https://www.amazon.com/gp/product/B005LW42MY/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [5V One Channel Relay Module](https://www.amazon.com/gp/product/B00LW15A4W/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [12V 2A Power Supply AC Adapter](https://www.amazon.com/gp/product/B086T1N5R4/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [Dupont Wire Set](https://www.amazon.com/gp/product/B07431WH2T/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

The Door:

(not sure about quantaty & size, will decide in-person at Home Depot) Plywood

(not sure about quantaty & size, will decide in-person at Home Depot) [Whitewood Stud](https://www.homedepot.com/p/2-in-x-4-in-x-8-ft-Prime-Whitewood-Stud-058449/312528776)

2x [Door hinge](https://www.homedepot.com/p/Everbilt-3-1-2-in-Satin-Nickel-Square-Corner-Door-Hinge-14982/202558075)

4x [Zinc Plated Corner Brace](https://www.homedepot.com/p/Everbilt-1-1-2-in-Zinc-Plated-Corner-Brace-Value-Pack-20-Pack-18564/202034301)

2x [Shelf Bracket](https://www.homedepot.com/p/Everbilt-10-in-x-8-in-Black-Medium-Duty-Shelf-Bracket-14287/206091422)

2x [Sandbag](https://www.homedepot.com/p/Sunnydaze-Decor-Polyester-Sandbag-Canopy-Weights-in-Black-Set-of-4-WUY-080/319228352?)

### Risks/Contingencies & Fall-back Plan

I did a fair amount of research on the doability of this project, and I am confident I can make it work. However, if I encounter issues such as one of the methods cannot be achieved, I will leave it out and implement the other two. 

## Functioning Project

![final product](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/final_product.jpg)

## Documentation of Design Process

### Verplank Diagram

![verplank diagram](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/verplank%20diagram.jpg)

### Storyboards

#### Scenario 1: 
![storyboard 1](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/storyboard%201.jpeg)

#### Scenario 2: 
![storyboard 2](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/storyboard%202.jpeg)

#### Scenario 3: 
![storyboard 3](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/storyboard%203.jpeg)

#### Scenario 4: 
![storyboard 4](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/storyboard%204.jpeg)

### Wiring Diagram

![wiring diagram](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/wiring_diagram.jpg)

### Door Design

![door design](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/door%20design.jpg)

## Archive of All Code and Design Patterns

#### Please view my source code [here](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/electromagnetic_lock.py).

#### Connect Parts & Sensors

![documentation](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/documentation.jpeg)

#### Tech Demo (Functional Checkoff) - click on image to watch video

[<img src="https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/tech.png" width="50%">](https://www.youtube.com/watch?v=vm3P7I4BzaE "Tech Demo")

#### Make the door & attach device

![documentation-door](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/documentation-door.jpg)

## Video Demo

## Reflections on Process

I began this project by sketching out detailed design plans. I started by writing a high-level summary of why I'm making this device, how it works, and how it will address real-world user pain points, and I developed a Verplank diagram based on this information. I also illustrated the various use cases of my device and the scenarios in which each of my lock's functionality works best in the storyboards. I presented this proposal to the IDD class and received feedback from the teaching team and peers. 

The next step of the design stage is developing a detailed wiring diagram and a design for the door -- these graphs show every detail of how the hardware of my lock would work. I tried to resolve all issues in design during this stage before implementing them physically. 

The biggest challenge I faced was connecting and programming the device's hardware. I had little background in hardware and had to learn everything, from soldering and connecting GPIOs with different sensors using Dupont wires to programming the hardware parts, all from scratch. During this process, I encountered the problem of not being able to connect my AS608 fingerprint module correctly to the pi. It took me about a week to debug -- from checking my code to changing the system settings of my pi. I even re-burned the image to my micro-SD card. It ended up that GPIO14(TX) and GPIO15(RX) on my pi were not working properly. To resolve this, I ordered a USB to TTX module and used it to connect my fingerprint module to my pi. This is an excellent example of how my limited experience in working with hardware affected the development of my project. Next time when I work with hardware, I will remember to test the hardware first.

After making the device, I made the door and attached my device to it. I did not encounter any problems in woodworking because I had extensive experience working with wood.

Along the way, I kept good documentation of the entire making process of my device using drawings, texts, and photographs. I also did a simple photoshoot (front and back view) for my device in a lightbox, and shot a demo video to demonstrate a user interacting with it.

## Group Work Distribution

This is not a group project. The design & development of this device were all done by Jiaqi.

Actor credits for video demo:


