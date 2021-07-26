from demo_clock import trigger2, ntptime, utime
import fire

def trigger1(func,hour,start,end, count):
    start = hour + 4
    while True:
        if utime.gmtime()[4] >= start and utime.gmtime()[4] <=end:
            for x in range(count):
                func()

trigger1(fire.main,10,25,28,3)
