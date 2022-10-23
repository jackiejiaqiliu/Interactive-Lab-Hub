# Observant Systems

**NAMES OF COLLABORATORS HERE**

I did not collaborate with anyone.

## Overview

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### Contours Detection

Design idea: Contours detection can be used for making computer-generated line drawings. If we only keep the contour lines in the image, we are able to turn an image into an abstract line drawing. We can also design a control panel that allows the user to adjust the width, color, and type of the strokes to make the drawing more personalized and creative.

![Contours Detection](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contours%20detection.png)

#### Face Detection

Design idea: This is more of an interactive art idea rather than a design idea that can help with a specific task in our daily lives. In the show "Person of Interest", the government develops a secret system, a machine that spies on everyone every hour of every day. The system gets information from every device that has an audio or video input that is connects to the internet -- from our own smartphones and laptops to the security cameras on the streets or in stores. I believe this kind of surveillance not only exists in this tv show, but also exists in the world we live in today. However, because many devices' surveillance feature is not visible, many people do not feel being "watched". So I wish to make an interactive art piece to discuss this issue. In an exhibition space, all the devices' audio or video input will be costumed to look like a human eye or ear. For example, the security camera or the two cameras on everyone's cellphone will look like an actual human eye. Utilizing face detection, the eyes follow the faces they see and stare at people. This piece should cause discomfort, raising awareness on surveillance and generate discussions.

![Face Detection](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%205/face%20detection.png)

#### Flow Detection

Design idea: This idea get inspirations from the [light painting technique in photography](https://www.canon-europe.com/get-inspired/tips-and-techniques/light-painting-photography/). Currently, the model detects feature points automatically, but if we can make it custom (for example, allow user to select feature points manually), we can make this kind of light painting with the movement of anything, without a light source and long-exposure photography.

![Flow Detection](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%205/flow%20detection.png)

#### Object Detection

Design idea: My desk gets messy very easily. Utilizing this object detection model, I can remind myself to clean up when neccessary. Whenever the number of object detected on the desk exceed a certain number, there will be a reminder for me to organize my desk.

![Object Detection](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%205/object%20detection.png)

#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
