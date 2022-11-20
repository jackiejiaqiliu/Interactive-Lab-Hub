# Final Project

[Project Plan](#project-plan) 

[Documentation of Design Process](#documentation-of-design-process) 

[Archive of All Code and Design Patterns](#archive-of-all-code-and-design-patterns) 

[Video Demo](#video-demo) 

[Reflections on Process](#reflections-on-process) 

[Group Work Distribution Questionnaire](#group-work-distribution-questionnaire) 

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

1x [12V/24V to 5V Step Down Converter](https://www.amazon.com/gp/product/B09DGFR24W/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [12V 2A Power Supply AC Adapter](https://www.amazon.com/gp/product/B086T1N5R4/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

1x [Dupont Line Set](https://www.amazon.com/gp/product/B07431WH2T/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)

The Door:

(not sure about quantaty & size, will decide in-person at Home Depot) Plywood

(not sure about quantaty & size, will decide in-person at Home Depot) [Whitewood Stud](https://www.homedepot.com/p/2-in-x-4-in-x-8-ft-Prime-Whitewood-Stud-058449/312528776)

4x [Zinc Plated Corner Brace](https://www.homedepot.com/p/Everbilt-1-1-2-in-Zinc-Plated-Corner-Brace-Value-Pack-20-Pack-18564/202034301)

2x [Shelf Bracket](https://www.homedepot.com/p/Everbilt-10-in-x-8-in-Black-Medium-Duty-Shelf-Bracket-14287/206091422)

2x [Sandbag](https://www.homedepot.com/p/Sunnydaze-Decor-Polyester-Sandbag-Canopy-Weights-in-Black-Set-of-4-WUY-080/319228352?)

### Risks/Contingencies & Fall-back Plan

I did a fair amount of research on the doability of this project, and I am confident I can make it work. However, if I encounter issues such as one of the methods cannot be achieved, I will leave it out and implement the other two. 


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

![wiring diagram](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/wiring%20diagram.JPG)

## Archive of All Code and Design Patterns

## Video Demo

## Reflections on Process

## Group Work Distribution Questionnaire
