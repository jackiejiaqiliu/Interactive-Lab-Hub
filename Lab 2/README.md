# Interactive Prototyping: The Clock of Pi

**Please indicate anyone you collaborated with on this Lab here.**

I did not collaborate with anyone.

## Prep

1. ### Set up your Lab 2 Github

2. ### Get Kit and Inventory Parts

   Please find my inventory list [here](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%202/partslist.md).

3. ### Prepare your Pi for lab this week


## Overview

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)


## Part A. 

Done. Nothing to report.

## Part B. 

Done. Nothing to report.


## Part C. 

Done. Nothing to report.

## Part D. 
### Set up the Display Clock Demo

https://user-images.githubusercontent.com/90330977/189428400-533f7fd1-59f4-4f91-8b95-b3f8dabd9a6d.mp4

## Part E.
### Modify the barebones clock to make it your own

My clock divides the minutes and hours of a day into boxes and rows on a canvas (each row represents an hour, each box in the row represents a minute). The boxes will show up one by one each minute. They are filled with different shades of blues, creating an overall gradient image that presents the progress of the day from dawn till dusk. The user can press the bottom button on the Adafruit MiniPiTFT at any point during the day, and a heart-warming message corresponding to the current time will greet the user, along with a digital clock that shows the exact time.

Please find the source code [here](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%202/screen_clock.py).

![Verplank digram](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%202/IDD%20Lab%202%20Part%201E%20-%20Verplank%20Diagram.jpg)

## Part F. 
### Make a short video of your modified barebones PiClock

https://user-images.githubusercontent.com/90330977/189429622-e52bc4b2-e949-48e9-9eac-72dc1a86ceb7.mp4

## Part G. 
### Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

Add a personalized feature that allows the user to change the gradient color:

By default, the gradient color will be determined by the current season (green - spring, red - summer, orange - fall, winter - blue).

However, if the user feels like the weather on that day feels like another season (for example, a very cold day in the fall that feels like winter), they can presses the top button on miniPiTFT, and change it to the color that fits their current feeling.

![gradient colors](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%202/IDD%20Lab%202%20Part%201G%20-%20Gradient%20Colors.png)


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 


