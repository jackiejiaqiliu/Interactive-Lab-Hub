# Chatterboxes
**NAMES OF COLLABORATORS HERE**

I did not collaborate with anyone.

## Part 1.

### Text to Speech 

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*

Please find my shell file [here](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%203/greet_by_name.sh).

### Speech to Text

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Please find my shell file [here](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/tree/Fall2022/Lab%203/numerical_input).

### Serving Pages

### Storyboard

\*\***Verplank Diagram**\*\*

![Verplank digram](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%203/IDD%20Lab%203%20-%20Verplak%20Diagram.jpg)

\*\***Script / Flowchart**\*\*

![Script Flow Chart](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%203/IDD%20Lab%203%20-%20Script:Flowchart.jpg)

\*\***Storyboard**\*\*

![Storyboard](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%203/IDD%20Lab%203%20-%20Storyboard.jpg)

\*\***Please describe and document your process.**\*\*

At first, I was thinking about creating a voice game that relies heavily on voice recognition. However, after testing out the voice-recognition software we are using for this lab, I realized that it is not accurate enough for that game. So I switched to this current idea that uses minimal voice recognition but a lot of voice recordings. 

I started by coming up with the Verplank diagram -- understanding what problem this device solves and how exactly it will solve it. Basically, it is a voice memo device that allows users to record short messages for themselves and replay them whenever needed later on. Since all interactions are voice-based, and the flow of logic follows a decision tree that has multiple levels, I found it helpful to come up with a script/flowchart to comb through the logic before drawing the storyboard.

### Acting out the dialogue

Note: I did not get to this part during Thursday's lab and did not have the chance to get a partner. So I tested my interaction with a user who is not part of our class over the weekend. I will try my best to test my interactions with classmates in the remaining parts of this lab.

https://user-images.githubusercontent.com/90330977/192116573-c20feefb-efb1-4083-b878-d20057597f1c.mp4

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

The majority of the conversations have been similar to what I expected. One deviation from expectation was when all existing messages had been played, the user wouldn't wait for the device to return to the main menu and repeat the instructions. A solution would be to give the user the option to directly record a new message at this point.

Also, I found the instructions a little repetitive when after acting out. However, I still choose to prioritize clarity over succinctness, as I believe knowing the instruction throughout the interation is essential in this voice-only system.

\*\***Updated Script / Flowchart after acting out**\*\*

![Updated Script Flow Chart](https://github.com/jackiejiaqiliu/Interactive-Lab-Hub/blob/Fall2022/Lab%203/IDD%20Lab%203%20-%20Updated%20Script:Flowchart.jpg)

### Wizarding with the Pi (optional)

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

Since my device is voice-only, and I can achieve the desired result with voice instruction, detection and recording through programming, I do not think wizarding is neccessary for my design.

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

\*\***1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...**\*\*

Wording - Since this is a voice-only device, I paid extra attention to the dialogue when I designed the interactions so that the instructions are clear and easy to understand. At this point, I do not think there's much to change.

Timing - I adjusted the recording time of each .sh file. I made the recordings for all the one-word answers 2 seconds and the recordings for the voice messages 5 seconds. This way the user does not need to wait too long after they say the keyword and will have enough time to finish their short messages.

Anticipation of misunderstanding - I wrote an else statement for all keyword recognition. So if the device fails to recognize the keyword said by the user, it will notify the user and prompt for a keyword again.

\*\***2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?**\*\*

To exit the program, the user can either say the word "quit" or wave the Accelerometer attached to the device. These two ways of interaction are both clearly stated in the voice instruction provided by the device

\*\***3. Make a new storyboard, diagram and/or script based on these reflections.**\*\*

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

\*\***Document how the system works**\*\*

This device is a voice memo device that allows users to record short messages for themselves and replay them whenever needed later on. The device provides a clear set of instructions through voice. It allows the user to play existing messages, record new messages, delete current messages, and quit the system by speaking the corresponding keyword to the device. Besides voice control, the user is also able to wave the sensor attached to the device to exit the program.

\*\***Include videos or screencaptures of both the system and the controller.**\*\*

My device is 100% voice-controlled so there is no controller.

https://user-images.githubusercontent.com/90330977/192949369-5bc9833f-3a5a-4f7c-9793-9241bc1c1b1e.mp4


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

