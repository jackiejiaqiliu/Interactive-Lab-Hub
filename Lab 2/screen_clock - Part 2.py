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

# colors for seasons
colors = ["#A1DA6D", "#DB736F", "#F8D57E", "#5F90F8"]

#get current month and decide starting value for count variable based on it
current_month = int(time.strftime("%m"))
if current_month in [3,4,5]:
    count = 0
elif current_month in [6,7,8]:
    count = 1
elif current_month in [9,10,11]:
    count = 2
elif current_month in [12,1,2]:
    count = 3

def drawCurrentTime(count):
    # define gradient colors
    greens = ["#E7FCD4","#DDF7C4","#D4F3B8","#CCEFAC","#C1EA9C","#BBE792","#B1E284","#A9DF78","#A1DA6D","#97D55E","#8DCA56","#83BF4E","#77B245","#6DA63E","#659D37","#5A9030","#508528","#467921","#44751F","#416F1E","#3D691B","#3B651A","#385F18","#355916"]
    reds = ["#F4BFBE","#F1B6B5","#EDAAA8","#EBA2A0","#E79795","#E5908E","#E18482","#DE7C79","#DB736F","#D96A66","#D6645F","#D45D57","#D1544E","#CD4D45","#CA433B","#C83E36","#C2332A","#B52E25","#A12820","#8B201A","#7E1C16","#6B1610","#570F0B","#4C0B07"]
    yellows = ["#F8E69D","#F8E193","#F8DE8E","#F8DA86","#F8D57E","#F7D076","#F7CD70","#F7C969","#F5C462","#EEBC5B","#EBB656","#E6AF50","#E0A84A","#DDA245","#D99D40","#D4953A","#D09135","#C68731","#BC7C2D","#B3732A","#A86925","#A06022","#995A1F","#8F4F1B"]
    blues = ["#D1E7FD","#C0DBFC","#AFCEFB","#A1C2FA","#91B7FA","#81AAF9","#6F9CF8","#5F90F8","#5085F7","#3D78F6","#376BE6","#315CD2","#2C4DC5","#273FB6","#2131A4","#1C2394","#161784","#120E77","#170D73","#1E0E70","#24106F","#2B116C","#30136B","#371569"]

    # draw an off-white background
    draw.rectangle((0, 0, width, height), outline="#faf5ed", fill="#faf5ed")
    
    # get current hour and minute
    current_h = int(time.strftime("%H"))
    current_m = int(time.strftime("%M"))
    
    # draw out the image for current time with selected (or default) gradient color
    if count % 4 == 0:
        for i in range(current_h):
            draw.rectangle((0, height/24*i, width, height/24*(i+1)), outline=greens[i], fill=greens[i])
        draw.rectangle((0,height/24*(current_h),width/60*(current_m),height/24*(current_h+1)),outline=greens[current_h], fill=greens[current_h])
    elif count % 4 == 1:
        for i in range(current_h):
            draw.rectangle((0, height/24*i, width, height/24*(i+1)), outline=reds[i], fill=reds[i])
        draw.rectangle((0,height/24*(current_h),width/60*(current_m),height/24*(current_h+1)),outline=reds[current_h], fill=reds[current_h])
    elif count % 4 == 2:
        for i in range(current_h):
            draw.rectangle((0, height/24*i, width, height/24*(i+1)), outline=yellows[i], fill=yellows[i])
        draw.rectangle((0,height/24*(current_h),width/60*(current_m),height/24*(current_h+1)),outline=yellows[current_h], fill=yellows[current_h])
    elif count % 4 == 3:
        for i in range(current_h):
            draw.rectangle((0, height/24*i, width, height/24*(i+1)), outline=blues[i], fill=blues[i])
        draw.rectangle((0,height/24*(current_h),width/60*(current_m),height/24*(current_h+1)),outline=blues[current_h], fill=blues[current_h])
    

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
    
    # draw out current image
    drawCurrentTime(count)
    
    # when button A is pressed
    if buttonB.value and not buttonA.value:
        count += 1
        
        # display and change gradient color + short message about season
        if count % 4 == 0:
            draw.rectangle((0, 0, width, height), outline=colors[0], fill=colors[0])
            y = (font.getsize("feels like")[1])*3
            x = int(width/2-font.getsize("feels like")[0]/2)
            draw.text((x, y), "feels like", font=font, fill="#FFFFFF")
            y += (font.getsize("feels like")[1])
            x = int(width/2-font.getsize("Spring")[0]/2)
            draw.text((x, y), "Spring", font=font, fill="#FFFFFF")
        elif count % 4 == 1:
            draw.rectangle((0, 0, width, height), outline=colors[1], fill=colors[1])
            y = (font.getsize("feels like")[1])*3
            x = int(width/2-font.getsize("feels like")[0]/2)
            draw.text((x, y), "feels like", font=font, fill="#FFFFFF")
            y += (font.getsize("feels like")[1])
            x = int(width/2-font.getsize("Summer")[0]/2)
            draw.text((x, y), "Summer", font=font, fill="#FFFFFF")
        elif count % 4 == 2:
            draw.rectangle((0, 0, width, height), outline=colors[2], fill=colors[2])
            y = (font.getsize("feels like")[1])*3
            x = int(width/2-font.getsize("feels like")[0]/2)
            draw.text((x, y), "feels like", font=font, fill="#FFFFFF")
            y += (font.getsize("feels like")[1])
            x = int(width/2-font.getsize("Fall")[0]/2)
            draw.text((x, y), "Fall", font=font, fill="#FFFFFF")
        elif count % 4 == 3:
            draw.rectangle((0, 0, width, height), outline=colors[3], fill=colors[3])
            y = (font.getsize("feels like")[1])*3
            x = int(width/2-font.getsize("feels like")[0]/2)
            draw.text((x, y), "feels like", font=font, fill="#FFFFFF")
            y += (font.getsize("feels like")[1])
            x = int(width/2-font.getsize("Winter")[0]/2)
            draw.text((x, y), "Winter", font=font, fill="#FFFFFF")
            
    # when button B is pressed
    elif buttonA.value and not buttonB.value:  # just button B pressed
        # set background to black
        draw.rectangle((0, 0, width, height), outline="black", fill="black")
        
        # get current time
        current_time = time.strftime("%m/%d/%Y  %H:%M")
        current_h = int(time.strftime("%H"))
        
        # choose message based on current time
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
        
        # display current time + greeting message
        y = top
        x = int(width/2-font.getsize(current_time)[0]/2)
        draw.text((x, y), current_time, font=font, fill="#696969")
        y += (font.getsize(current_time)[1])*3
        x = int(width/2-font.getsize(statement)[0]/2)
        draw.text((x, y), statement, font=font, fill="#FFFFFF")
        
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
    
