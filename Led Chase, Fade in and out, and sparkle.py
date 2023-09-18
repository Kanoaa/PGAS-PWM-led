
import time
import neopixel 
import board
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = .5)

bckg_color = [255, 0, 0]

sprk_color = [255, 255, 255]

color = [255, 0, 255]

off = [0, 0, 0]

"""
Function name is fade_out

This function makes the led strip fade in and out making the color of the led [0, 0, 0]

The parameters are color_fade which is a set list and delay which is a float

The return value of the definition is the color value

"""

def fade_out(color_fade = [255, 0, 255], delay = 0.01):
    red_value = float(color_fade[0] / 256) 
    green_value = float(color_fade[1] / 256)
    blue_value = float(color_fade[2] / 256) 
    for i in range(255):
        color_fade[0] = (color_fade[0] - red_value) % 255
        color_fade[1] = (color_fade[1] - green_value) % 255
        color_fade[2] = (color_fade[2] - blue_value) % 255
        np.fill((int(color_fade[0]), int(color_fade[1]), int(color_fade[2])))
        np.show()
        print(color_fade)
        time.sleep(delay)
    
"""
Function name is fade_in

This function makes the led strip fade out making the color of the led [0, 0, 0] and setting it to the maximum brightness

The parameters are color_fade which is a set list and delay which is a float

The return value of the definition is the color value

"""
def fade_in(color_fade = [255, 0, 255], delay = 0.01):
    red_value = float(color_fade[0] / 256) 
    green_value = float(color_fade[1] / 256)
    blue_value = float(color_fade[2] / 256) 
    for i in range(255):
        color_fade[0] = (color_fade[0] + red_value) % 255
        color_fade[1] = (color_fade[1] + green_value) % 255
        color_fade[2] = (color_fade[2] + blue_value) % 255
        np.fill((int(color_fade[0]), int(color_fade[1]), int(color_fade[2])))
        np.show()
        print(color_fade)
        time.sleep(delay)


    
"""
The function name is sparkle

The function makes the led strip be set to one color and it randomizes the amount of sparkles you want into the color white within the set color

The parameters are the sparkle color (sprk_color), background color (bckg_color), the delay of each 

The definition returns the "sparkle" that is a different set of leds in a color standing out of the main color
"""
def sparkle(sprk_color, bckg_color, delay = 0.01, num_sprk = 1, speed = 0.05):
    for i in range(50):
        np.fill(color)
        for j in range(num_sprk):
            rand = random.randint(0, 29)
            np[rand] = sprk_color
        time.sleep(speed)
        np[rand] = bckg_color
        np.show()
        
        
"""
The fucntion name is chase

The funtion sets every other two neppixels to either off ([0, 0, 0]) or the color that you want to be show. Then the code repeats this for the nect neopixel making them "follow" each other down the strip.

The parameters are color which is the other two neopxiels that aren't turned on and delay which is giving a delay on the code running each neopixel.

The return value is every other two neopixels being shown and them travling around the led strip
"""
def chase(color = [0,0,0], delay = 0.01):
    for j in range(50):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30
                np[led] = [0, 255, 255]
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
            time.sleep(delay)
    
    
while True:
    sparkle(sprk_color, color, 0.01, 5)
    fade_out()
    fade_in()
    chase(off, 0.01)
    fade_in()
    sparkle(sprk_color, color, 0.01, 5)

    

    

        
    
