###############################################################################
# Filename    : Os2.py
# Date        : 07/27/2020 
# Description : Controls tasks and environment algorithms. 
###############################################################################

import asyncio
import time
from datetime import datetime
from periodic import Periodic


async def periodic_10s_tasks(param):
    print(datetime.now(), 'Yay!', param)
    await asyncio.sleep(10)

async def periodic_30s_tasks(param):
    print(datetime.now(), 'Yay!', param)
    await asyncio.sleep(30)
    
async def periodic_60s_tasks(param):
    print(datetime.now(), 'Yay!', param)
    await asyncio.sleep(60)

async def main():
    Loop_10s = Periodic(1, periodic_10s_tasks, '10s_loop')
    await Loop_10s.start()
    Loop_30s = Periodic(3, periodic_30s_tasks, '30s_loop')
    await Loop_30s.start()
    Loop_60s = Periodic(6, periodic_60s_tasks, '60s_loop')
    await Loop_60s.start()
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
    
