###############################################################################
# Filename    : Plug.py
# Date        : 07/27/2020 
# Description : Controls TPLink Smart Plugs
###############################################################################

import asyncio
from kasa import SmartPlug

plug1_ip = '10.0.0.69'
plug2_ip = '10.0.0.167'

async def turn_plug1_on():
    global plug1_ip
    plug1 = SmartPlug(plug1_ip)
    await plug1.update()
    await plug1.turn_on()

async def turn_plug1_off():
    global plug1_ip
    plug1 = SmartPlug(plug1_ip)
    await plug1.update()
    await plug1.turn_off()
    
async def turn_plug2_on():
    global plug2_ip
    plug2 = SmartPlug(plug2_ip)
    await plug2.update()
    await plug2.turn_on()

async def turn_plug2_off():
    global plug2_ip
    plug2 = SmartPlug(plug2_ip)
    await plug2.update()
    await plug2.turn_off()

def plug1_on():
    asyncio.run(turn_plug1_on())
    
def plug1_off():
    asyncio.run(turn_plug1_off())
    
def plug2_on():
    asyncio.run(turn_plug2_on())
    
def plug2_off():
    asyncio.run(turn_plug2_off()) 