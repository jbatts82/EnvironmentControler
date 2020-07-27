###############################################################################
# Filename    : Os2.py
# Date        : 07/27/2020 
# Description : Controls tasks and environment algorithms. 
###############################################################################

import asyncio
import time

async def main():
    T10s = asyncio.create_task(task10s())
    T30s = asyncio.create_task(task30s())
    T60s = asyncio.create_task(task60s())
    await T10s
    await T30s
    await T60s

async def task10s():
    await asyncio.sleep(1)
    print("10s")
    print(f"time is {time.strftime('%X')}")
    
async def task30s():
    await asyncio.sleep(3)
    print("30s")
    print(f"time is {time.strftime('%X')}")
    
async def task60s():
    await asyncio.sleep(6)
    print("60s")
    print(f"time is {time.strftime('%X')}")

while True:
    asyncio.run(main())
    
