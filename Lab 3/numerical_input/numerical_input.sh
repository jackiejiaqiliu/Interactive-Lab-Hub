#from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f2 -k5 -s150 --stdout "What is your zipcode?" | aplay

#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

arecord -D hw:2,0 -f cd -c1 -r 16000 -d 5 -t wav answer.wav
python3 test_words.py answer.wav
