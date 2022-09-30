import pygame
import os

os.system('sh intro.sh')
messages = []


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

def play_message(message):
    pygame.mixer.init()
    pygame.mixer.music.load(message)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        continue
            
while True:
    os.system('sh fake_main.sh')
    answer = input("answer: ")

    if answer == "n":
        new()

    elif answer == "p":
        if len(messages) == 0:
            os.system('sh fake_no_message.sh')
            no_message_answer = input("new message: ")
            if no_message_answer == "n":
                new()
            else:
                os.system('sh error.sh')
        else:
            count = 0
            for i in messages:
                play_message(i)
                os.system('sh fake_process_message.sh')
                process_answer = input("process message: ")
                if process_answer == "n":
                    if count == len(messages)-1:
                        os.system('sh no_more_message.sh')
                        break
                elif process_answer == "d":
                    messages.pop(count)
                    os.system('sh delete_success.sh')
                    print(messages)
                    break
                else:
                    os.system('sh error.sh')
                    break
                count += 1
      
    elif answer == "q":
        os.system('sh bye.sh')
        break
    
    else:
        os.system('sh error.sh')
 
        
