###############################################################################
# Filename    : Plug.py
# Date        : 07/27/2020 
# Description : Controls TPLink Smart Plugs
###############################################################################

import asyncio
from kasa import SmartPlug
from time import sleep

plug1_ip = '10.0.0.69'
plug2_ip = '10.0.0.168'

# private functions

async def init_the_plugs():
    global plug1, plug2
    global plug1_error_state, plug2_error_state

    try:
        plug1 = SmartPlug(plug1_ip)
        await plug1.update()
    except:
        plug1_error_state = True
    else:
        plug1_error_state = False
       
    try:
        plug2 = SmartPlug(plug2_ip)
        await plug2.update()
    except:
        plug2_error_state = True
    else:
        plug2_error_state = False
 
async def turn_plug1_on():
    global plug1
    await plug1.turn_on()

async def turn_plug1_off():
    global plug1
    await plug1.turn_off()

async def turn_plug2_on():
    global plug2
    await plug2.turn_on()

async def turn_plug2_off():
    global plug2
    await plug2.turn_off()

async def is_plug1_on():
    global plug1
    await plug1.update()
    return plug1.is_on
    
async def is_plug2_on():
    global plug2
    await plug2.update()
    return plug2.is_on
    
async def get_plug1_info():
    global plug1
    print(plug1.alias)
    print(plug1.model)
    print(plug1.rssi)
    print(plug1.mac)
    
async def get_plug2_info():
    global plug2
    print(plug2.alias)
    print(plug2.model)
    print(plug2.rssi)
    print(plug2.mac)

# Public Interfaces

def init_plug():
    asyncio.run(init_the_plugs())

def get_plug1_state():
    try:
        plug1_state = asyncio.run(is_plug1_on())
    except:
        plug1_state = "Error"
        init_plug()
    return plug1_state

def get_plug2_state():
    try:
        plug2_state = asyncio.run(is_plug2_on())
    except:
        plug2_state = "Error"
        init_plug()
    return plug2_state

def plug1_info():
    asyncio.run(get_plug1_info())
    
def plug2_info():
    asyncio.run(get_plug2_info())

def plug1_on():
    asyncio.run(turn_plug1_on())
    
def plug1_off():
    asyncio.run(turn_plug1_off())
    
def plug2_on():
    asyncio.run(turn_plug2_on())
    
def plug2_off():
    asyncio.run(turn_plug2_off()) 