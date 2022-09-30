import pygame
import os
import time
import board
from adafruit_msa3xx import MSA311

#play intro message
os.system('sh intro.sh')

# list to keep track of messages
messages = []


# function to record new message. There is only space for up to 3 messages.
def new():
    if len(messages) == 0: 
        os.system('sh new1.sh')
        os.system('sh record_success.sh')
        messages.append("message1.wav")
    elif len(messages) == 1: 
        os.system('sh new2.sh')
        os.system('sh record_success.sh')
        messages.append("message2.wav")
    elif len(messages) == 2:
        os.system('sh new3.sh')
        os.system('sh record_success.sh')
        messages.append("message3.wav")
    else:
        os.system('sh storage_full.sh')

# function to play messages (wav files) using pygame
def play_message(message):
    pygame.mixer.init()
    pygame.mixer.music.load(message)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        continue
        
# function to detect sensor movement
def sensor_movement():
    i2c = board.I2C()
    msa = MSA311(i2c)

    # initial position
    last_x = 0
    last_y = 0
    last_z = 0
    x,y,z = msa.acceleration
    last_x = x
    last_y = y
    last_z = z

    while True:
        # check for movement
        x,y,z = msa.acceleration
        if x - last_x >= 5 or last_x - x >= 5 or y - last_y >= 5 or last_y - y >= 5 or z - last_z >= 5 or last_z - z >= 5:
            return True
        last_x = x
        last_y = y
        last_z = z
        time.sleep(0.5)
            
while True:
    # play main menu instruction
    os.system('sh main.sh')
    
    # get answer from answer.txt file
    f = open("answer.txt","r")
    answer = f.read()

    # if the user wants to create a new message
    if answer == "new":
        new()

    # if the user wants to play existing messages
    elif answer == "play":
        # if currently no message, tell the user and let them decide whether or not create new message
        if len(messages) == 0:
            os.system('sh no_message.sh')
            # get user's answer from answer.txt
            f = open("answer.txt","r")
            no_message_answer = f.read()
            # if the user chooses to create a new message, create one.
            if no_message_answer == "new":
                new()
            else:
                os.system('sh error.sh')
        # if currently have messages
        else:
            count = 0
            # loop through all messages
            for i in messages:
                # play the current message
                play_message(i)
                # ask the user whether to delete the current message or play the next one
                os.system('sh process_message.sh')
                # get user's answer from answer.txt
                f = open("answer.txt","r")
                process_answer = f.read()
                # if user chooses to play the next message
                if process_answer == "next":
                    # if there is no more messages, notify user
                    if count == len(messages)-1:
                        os.system('sh no_more_message.sh')
                        break
                # if user chooses to delete current message, remove current message from list
                elif process_answer == "delete":
                    messages.pop(count) 
                    os.system('sh delete_success.sh')
                    break
                # the system does not understand any other answers
                else:
                    os.system('sh error.sh')
                    break
                count += 1
                
    # if the user says "quit" or waves the sensor, say bye and quit program
    elif answer == "quit" or sensor_movement() == True:
        os.system('sh bye.sh')
        break
    
    # if the system fails to understand user's answer, notify user and ask again.
    else:
        os.system('sh error.sh')

        
