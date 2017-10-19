# -*- coding: utf-8 -*-
from com.samsung.stp.engine.TouchPressType import *
from stp_lib.devices import get_selected_device
from com.samsung.stp.engine import PythonListener

dev = get_selected_device()

def clb(a):
    print "Broadcast callback"
    print "Extras:"
    for x in a:
        print x,"=",a[x]

dev.setBroadcastCallback("android.intent.action.BATTERY_CHANGED", clb)
dev.sleep(10000)
dev.removeBroadcastCallback("android.intent.action.BATTERY_CHANGED")

dev.setTestResult(True)
