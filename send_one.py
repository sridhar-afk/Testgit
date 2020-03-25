# coding: utf-8

"""
This example shows how sending a single message works.
"""

from __future__ import print_function

import can
import time
##import os
##os.add_dll_directory(os.getcwd()


def send_one():

    # this uses the default configuration (for example from the config file)
    # see https://python-can.readthedocs.io/en/stable/configuration.html
    #bus = can.interface.Bus()

    # Using specific buses works similar:
    # bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    #bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)
    # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    bus = can.interface.Bus(bustype='vector', app_name='CANoe', channel=0, bitrate=500000)
    # ...

    msg = can.Message(
        arbitration_id=0x12, data=[11,22,33], is_extended_id=False
    )
    print(msg)
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
        
    except can.CanError:
        print("Message NOT sent")

    msg1 = can.Message(
        arbitration_id=0x13, data=[44,55,66], is_extended_id=False
    )
    print(msg1)
    try:
        bus.send(msg1)
        print("Message sent on {}".format(bus.channel_info))
        
    except can.CanError:
        print("Message NOT sent")

    msg2 = can.Message(
        arbitration_id=0x14, data=[77,88,99], is_extended_id=False
    )
    print(msg2)
    try:
        bus.send(msg2)
        print("Message sent on {}".format(bus.channel_info))
        
    except can.CanError:
        print("Message NOT sent")

        
    #task = bus.send_periodic(msg,2)

    #time.sleep(10)
    #task.stop(10)
        
    '''msg = can.Message(
        arbitration_id=0x14, data=[44,55,66], is_extended_id=False
    )

    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
        
    except can.CanError:
        print("Message NOT sent")
    task = bus.send_periodic(msg,5)'''


if __name__ == "__main__":
    send_one()
