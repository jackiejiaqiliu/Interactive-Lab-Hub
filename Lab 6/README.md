# Little Interactions Everywhere

I did part A-D on my own. I did part E with Runze Zhang(rz387) and Hongjiao Zhang(hz452).

## Overview

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

Nothing to submit

### Part B
### Send and Receive on your Pi

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

![idea 1](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/idea%201.jpg)

![idea 2](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/idea%202.jpg)

![idea 3](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/idea%203.jpg)

![idea 4](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/idea%204.jpg)

![idea 5](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/idea%205.jpg)


### Part C
### Streaming a Sensor

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

![setup](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/setup.JPG)

![mqtt](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/twizzlers%20MQTT.png)

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

![setup](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/setup-button.jpg)

![mqtt](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/mqtt-button.png)


### Part D
### The One True ColorNet

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

![part-d-1](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/part-d-1.jpg)

![part-d-2](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/part-d-2.png)

### Part E
### Make it your own

I did this part with Runze Zhang(rz387) and Hongjiao Zhang(hz452).

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

Our design is gesture remote control to switch slides back and forth. We think it is very necessary and cool to implement this design because every presenter face the challenge of how to switching slides smoothly while maintain good reliability. Sometimes a remote control device might be out of battery or too long of a distance or might just be the presenter forgets to bring a remote control. That way it would be very difficult to move on with their presentations. With our design, we can remotely control the presentation moving forward and backward with simple gestures to make presenters’ lives much easier.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

![part-e-plan](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%206/part%20e%20plan.jpg)

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

Our design is very easy in terms of user interface. If users encounter our design, they only need to wave their hands up/down or left/right to the gesture sensor to suggest which remote signals they want to send, and raspberry pi would help them to inform the server side to move to previous or next slide of the presentation slides. Up/left means previous slide and down/right means next slide.

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

https://user-images.githubusercontent.com/90330977/200382277-475639d2-ca78-4b81-abdb-42cb201dfb4c.mp4


