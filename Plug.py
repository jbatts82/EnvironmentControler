###############################################################################
# Filename    : Plug.py
# Date        : 07/27/2020 
# Description : Controls TPLink Smart Plugs
###############################################################################

import asyncio
from kasa import SmartPlug
from kasa import Discover
from pprint import pformat as pf

plug1_ip = '10.0.0.69'
plug2_ip = '10.0.0.167'

def plug_init():
    global plug1, plug2
    plug1 = SmartPlug(plug1_ip)
    plug2 = SmartPlug(plug1_ip)

def discover_devices():
    devices = asyncio.run(Discover.discover())
    for addr, dev in devices.items():
        asyncio.run(dev.update())
        print(f"{addr} >> {dev}")   

def get_device_info(plug):
    asyncio.run(plug.update())
    print("Hardware: %s" % pf(plug.hw_info))
    print("Full sysinfo: %s" % pf(plug.sys_info))
    
def get_emeter_status(plug):
    print("Current consumption: %s" % await plug.get_emeter_realtime())
    print("Per day: %s" % await plug.get_emeter_daily(year=2016, month=12))
    print("Per month: %s" % await plug.get_emeter_monthly(year=2016))
    
def get_device_state():
    print("Current state: %s" % plug.is_on)

def get_plug1_state():
    global plug1
    return plug1.is_on

def plug1_on():
    await plug1.turn_on()

def plug1_off():
    await plug1.turn_off()

plug_init()
discover_devices()
get_device_info(plug1_ip)
get_device_info(plug1)
get_device_info(plug2)






