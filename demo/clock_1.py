import utime, machine, time
import ntptime
import neopixel

np = neopixel.NeoPixel(machine.Pin(16), 256)

ntptime.host = '3.north-america.pool.ntp.org'
ntptime.settime()

def trigger(start,end):
    while True:
        if utime.gmtime()[5] > start and utime.gmtime()[5] <=end:
            if start > end and end < 60:
                np[57] = (120,120,0)
                np.write()
            else:
                np[57] = (0,0,0)
                np.write()

def trigger2():
    while True:
        if utime.gmtime()[5] % 5 == 0:
            np[60] =(1 << 4, 1 << 4,0)
            np[76] = (0,0,0)
            np.write()
        else:
            np[60] =(0,0,0)
            np[76] = (120,0,180)
            np.write()

def bar_block(rw,color):
    for i in rw:
        np[i[0]],np[i[1]],np[i[2]],np[i[3]],np[i[4]],np[i[5]],np[i[6]],np[i[7]] = color
        np[i[0]+(8)],np[i[1]+(8)],np[i[2]+(8)],np[i[3]+(8)],np[i[4]+(8)],np[i[5]+(8)],np[i[6]+(8)],np[i[7]+(8)] = color
        np[i[0]+(8*2)],np[i[1]+(8*2)],np[i[2]+(8*2)],np[i[3]+(8*2)],np[i[4]+(8*2)],np[i[5]+(8*2)],np[i[6]+(8*2)],np[i[7]+(8*2)] = color
        np.write()

def bar_block(rw,color):
    for i in rw:
        np[i[0]],np[i[1]],np[i[2]],np[i[3]],np[i[4]],np[i[5]],np[i[6]],np[i[7]] = color
        np.write()
        time.sleep(.1)

def bar_clock():
    "create blocks of color"
    while True:
        bar_block((utime.gmtime()[4]+1)//2)
