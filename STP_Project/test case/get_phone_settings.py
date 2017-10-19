# -*- coding: utf-8 -*-
from com.samsung.stp.engine.TouchPressType import *
from stp_lib.devices import get_selected_device

dev = get_selected_device()

# set ring volume to 1
dev.setPhoneSetting("volume_ring", "1")

# check if ring volume was set correctly
dev.setTestResult(dev.getPhoneSettings("system", "volume_ring") == "1")