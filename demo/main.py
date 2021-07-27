#from demo_clock import ntptime, utime
import uasyncio as asyncio
from sched.sched import schedule
from time import localtime
import fire



async def main():
    print('Asynchronous test running...')
    asyncio.create_task(schedule(fire.main_w_clear, hrs=None, mins=range(0, 60, 5)))
    asyncio.create_task(schedule(fire.main, hrs=None, mins=range(0, 60, 2), times=1))
    await asyncio.sleep(900)  # Quit after 15 minutes

try:
    asyncio.run(main())
finally:
    _ = asyncio.new_event_loop()