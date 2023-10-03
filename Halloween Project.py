import time
import neopixel 
import board
import random

np = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write = False, brightness = .5)


fcolors = [(255, 0, 0), (255, 165, 0), (255, 50, 0), (255, 63, 0), (0, 0, 0)]

speed = [0.094, 0.071, 0.087, 0.062]

off = [0, 0, 0]

sprk_color = [255, 0, 0]

color = [255, 165, 0]
"""
Function - Fire

This function makes a random amount of pixels change different speeds and colors

There are no parameters (I didn't have time)

The return value is the random speed and color choices

"""
def fire():
    for i in range(50):
        np.fill(fcolors[0])
        for j in range(100):
            rand_int = random.randint(0, 9)
            np[rand_int] = random.choice(fcolors)
        np.show()
        time.sleep(random.choice(speed))
        np[rand_int] = fcolors[2]
        np.show()
    
"""
Function - Chase

This function makes every other two pixels follow each other.

There are color and delay

The return value is the random speed and color choices

"""

def chase(color = [0,0,0], delay = 0.01):
    for j in range(10):
        np.show()
        for i in range(10):
            if i % 3 != 0:
                led = (i+j) % 10
                np[led] = [255, 191, 0]
            elif i % 3 == 0:
                led = (i+j) % 10
                np[led] = color
            time.sleep(delay)

"""
Function -

"""

def sparkle(sprk_color, bckg_color, delay = 0.01, num_sprk = 1, speed = 0.05):
    for i in range(50):
        np.fill(color)
        for j in range(num_sprk):
            rand = random.randint(0, 9)
            np[rand] = sprk_color
        time.sleep(speed)
        np[rand] = bckg_color
        np.show()
        
pre_flash = [0, 0, 0]

time_off = [(0.05), (0.1), (0.7), (0.02)]

speed = [(0.046), (0.083), (0.097)]

lcolors = [(0, 0, 0,), (255, 255, 255)]

lbckg_color = [(128, 0, 128)]

def lightning():
    np.fill(pre_flash)
    np.show()
    time.sleep(0.2)
    np.fill(lcolors[1])
    np.show()
    for j in range(100):
        rand_int = random.randint(0, 9)
        np.fill(lcolors[0])
        time.sleep(random.choice(speed))
    np.show()
    time.sleep(0.01)

while True:
    fire()
    chase(off, 0.1)
    sparkle(sprk_color, color, 0.01, 5)
    lightning()
    
    
    
