from machine import Pin
import neopixel
from os import urandom
import gc

#This file is taken from 
#Tdicola
#https://gist.github.com/tdicola/63768def5b2e4e3a942b085cd2264d7b
# and presented here: https://www.youtube.com/watch?v=QcyuYvyvOEI
#who was inspired by
#https://lodev.org/cgtutor/fire.html


#PIXEL_PIN    = 16
#PIXEL_WIDTH   = 32
#PIXEL_HEIGHT  = 8
#FLAME_DIVISOR = 7.77


def hue2rgb(p, q, t):
    # Helper for the HSL_to_RGB function.
    # From: http://axonflux.com/handy-rgb-to-hsl-and-rgb-to-hsv-color-model-c
    if t < 0:
        t += 1
    if t > 1:
        t -= 1
    if t < 1/6:
        return p + (q - p) * 6 * t
    if t < 1/2:
        return q
    if t < 2/3:
        return p + (q - p) * (2/3 - t) * 6
    return p

def HSL_to_RGB(h, s, l):
    # Convert a hue, saturation, lightness color into red, green, blue color.
    # Expects incoming values in range 0...255 and outputs values in the same range.
    # From: http://axonflux.com/handy-rgb-to-hsl-and-rgb-to-hsv-color-model-c
    h /= 255.0
    s /= 255.0
    l /= 255.0
    r = 0
    g = 0
    b = 0
    if s == 0:
        r = l
        g = l
        b = l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)
    return (int(r*255.0), int(g*255.0), int(b*255.0))

# Fire matrix helper class to easily lookup and set 2D intensity values.
class FireMatrix:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [0]*(width*height)

    def get(self, x, y):
        x %= self.width   # Wrap around when x values go outside the bounds!
        y %= self.height  # Like-wise wrap around y values!
        return self.data[y * self.width + x]

    def set(self, x, y, value):
        x %= self.width
        y %= self.height
        self.data[y * self.width + x] = value

def clear():
    np.fill((0,0,0))
    np.write()

# Main loop:
def main():

    PIXEL_PIN    = 16
    PIXEL_WIDTH   = 32
    PIXEL_HEIGHT  = 8
    FLAME_DIVISOR = 7.77

    # Create a color palette of flame colors.
    ## avoid running our of memory, build incrementallly
    palette = [HSL_to_RGB(x//3,255,min(255,x*2))for x in range(64)]
    gc.collect()
    palette.extend(HSL_to_RGB(x//3,255,min(255,x*2))for x in range(64,128))
    gc.collect()
    palette.extend(HSL_to_RGB(x//3,255,min(255,x*2))for x in range(128,192))
    gc.collect()
    palette.extend(HSL_to_RGB(x//3,255,min(255,x*2))for x in range(192,256))
    gc.collect()

# Initialize neopixels.
    np = neopixel.NeoPixel(Pin(PIXEL_PIN), PIXEL_WIDTH*PIXEL_HEIGHT)
    np.fill((0,0,0))
    np.write()

# Create fire matrix.
    fire = FireMatrix(PIXEL_WIDTH, PIXEL_HEIGHT+1)
    
    for i in range(256):
    #while True:
        # Set the bottom row to random intensity values (0 to 255).
        for x in range(PIXEL_WIDTH):
            fire.set(x, PIXEL_HEIGHT, int(urandom(1)[0]))
        # Perform a step of flame intensity calculation.
        for x in range(PIXEL_WIDTH):
            for y in range(PIXEL_HEIGHT):
                value = 0
                value += fire.get(x-1, y+1)
                value += fire.get(x, y+1)
                value += fire.get(x+1, y+1)
                value += fire.get(x, y+2)
                value = int(value / FLAME_DIVISOR)
                fire.set(x, y, value)
        # Convert the fire intensity values to neopixel colors and update the pixels.
        for x in range(PIXEL_WIDTH):
            for y in range(PIXEL_HEIGHT):
                np[y * PIXEL_WIDTH + x] = palette[fire.get(x, y)]
        np.write()

def main_w_clear():
    main()
    clear()