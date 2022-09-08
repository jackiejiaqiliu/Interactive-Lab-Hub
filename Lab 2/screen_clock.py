import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def drawCurrentTime():
    draw.rectangle((0, 0, width, height), outline="#faf5ed", fill="#faf5ed")
    
    current_h = int(time.strftime("%H"))
    current_m = int(time.strftime("%M"))
    
    colors = ["#D1E7FD","#C0DBFC","#AFCEFB","#A1C2FA","#91B7FA","#81AAF9","#6F9CF8","#5F90F8","#5085F7","#3D78F6","#376BE6","#315CD2","#2C4DC5","#273FB6","#2131A4","#1C2394","#161784","#120E77","#170D73","#1E0E70","#24106F","#2B116C","#30136B","#371569"]
    
    for i in range(current_h):
        draw.rectangle((0, height/24*i, width, height/24*(i+1)), outline=colors[i], fill=colors[i])
    
    draw.rectangle((0,height/24*(current_h),width/60*(current_m),height/24*(current_h+1)),outline=colors[current_h], fill=colors[current_h])
    

while True:

    #LAB 2 PART 1 PART D - REGULAR CLOCK
    '''
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    title = "Current Date & Time"
    current_date = time.strftime("%m/%d/%Y")
    current_time = time.strftime("%H:%M:%S")

    y = top
    x = int(width/2-font.getsize(title)[0]/2)
    draw.text((x, y), title, font=font, fill="#696969")
    y += (font.getsize(title)[1])*3
    x = int(width/2-font.getsize(current_date)[0]/2)
    draw.text((x, y), current_date, font=font, fill="#FFFFFF")
    y += font.getsize(current_date)[1]
    x = int(width/2-font.getsize(current_time)[0]/2)
    draw.text((x, y), current_time, font=font, fill="#FFFFFF")
    
    '''
    
    #LAB 2 PART 1 PART E - CREATIVE CLOCK

    drawCurrentTime()
    
    if buttonA.value and not buttonB.value:  # just button B pressed
        draw.rectangle((0, 0, width, height), outline="black", fill="black")
        current_time = time.strftime("%m/%d/%Y  %H:%M")
        current_h = int(time.strftime("%H"))
        
        statement = ""
        if current_h >= 0 and current_h <= 5:
            statement = "Don't stay up too late!"
        elif current_h >= 6 and current_h <= 10:
            statement = "Good morning!"
        elif current_h >= 11 and current_h <= 12:
            statement = "Don't forget to eat lunch!"
        elif current_h >= 13 and current_h <= 16:
            statement = "Good Afternoon!"
        elif current_h >= 17 and current_h <= 20:
            statement = "It's dinner time!"
        elif current_h >= 21 and current_h <= 23:
            statement = "Time to go to bed!"
        
        y = top
        x = int(width/2-font.getsize(current_time)[0]/2)
        draw.text((x, y), current_time, font=font, fill="#696969")
        y += (font.getsize(current_time)[1])*3
        x = int(width/2-font.getsize(statement)[0]/2)
        draw.text((x, y), statement, font=font, fill="#FFFFFF")
        
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
    
