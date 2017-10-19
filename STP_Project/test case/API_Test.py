# -*- coding: utf-8 -*-

from stp_lib.devices import get_android_devices_manager, get_selected_device
from stp_lib import node
from stp_lib import *
from stp_lib.menu_tree.Runner import Runner
from stp_lib.project import Project
from com.samsung.stp.engine import DevicesManagerFactory
# from stp_lib.node import *
# "adb shell settings put system screen_off_timeout 30000"
# "adb shell settings get system screen_off_timeout 30000"
# "adb shell settings get global auto_time"



dev = get_selected_device()

from stp_lib.node import *
print scroll(u"人民币", 0, dev, ".*")

# for i in range(5):
#     dev.swipe(300, 300, 1000, 1000, 0)
#     dev.sleep(1000)

# dev.sendShellCommand("settings put system screen_off_timeout 600000")

''' not working? '''
# dev.setPhoneSetting("screen_off_timeout", "30000")

# node.scrollBottom(dev)

''' 一直都是list not found错误 , 所有scroll相关的方法怎么用？'''
# node.scrollBottom(dev)

# top = node.TopNode(dev)
# top.click_on_text(u".*亮度.*", dev)

''' 注意所有get_node_xx() 返回的是一个 list<node>，而不是单个list '''
# display = top.get_node_by_text(u"显示")
# print display[0].click(dev)

# display = top.get_node_by_text(u"中国")
# print display

# display = top.get_node_by_text(u"显示")
# display.click(dev)
# 
# top = TopNode(dev)
# 
# if top.get_node_by_text("91 ?1") == []:
#     print "Activity: ", dev.getTopActivity()


''' 给获取了focus的地方输入指定 字符，支持中文'''
# dev.setText(u"string中国") 

''' 未知两个命令的区别， 可以正常返回ping结果，公司wfif网络正常未知？ '''
# print dev.sendShellCommand("ping -c 1 -w 5 www.baidu.com") # 相当于以adb shell开头
# print dev.shell("ping -c 3 -w 5 www.baidu.com")
# 注意和shell的区别
# dev.debugBridgeCommand(u"devices", 2000) # 没有shell

''' MobileInsight, class node.Node(node, parent=None, level=0)[source] 用法'''


# devId = get_android_device_id_by_index(0)
# # it can be copied from DeviceView table by using right click
# 
# # we create a instance of manager which will control device status
# manager = DevicesManagerFactory.create("Android")
# manager.setWaitingForDevice(devId, True)  # waiting for device is now possible
# 
# dev.reboot(None, 120000)  # reboot command
# if dev.waitForDevice(1000):  # wait for device
#     dev.setTestResult(True)
# manager.setWaitingForDevice(devId, False)  # disable waiting function
# dev.sleep(30000)




# dev.setTestResult(False)
# ans = dev.startActivity(u"com.android.contacts/.activities.PeopleActivity")
# ans = dev.killActivity(u"com.android.contacts")
# if dev.waitForActivityDestroyed(u"com.android.contacts/.activities.PeopleActivity", 3000):
#     ans = dev.setTestResult(True)
#     print "destroyed"


# dev.turnBluetooth(True)



# print dev.takeSnapshot(10, 10) 

# dev.startLogger(u"AndroidLogger", u"logcat")
# dev.startLogger(u"AndroidPcktCapLogger", u"tcpdump")
# dev.startLogger(u"SilentLogger", u"silent")
# dev.run(u"Internet")
# dev.sleep(3000)
# dev.stopLogger(u"AndroidLogger")
# dev.stopLogger(u"AndroidPcktCapLogger")
# dev.stopLogger(u"SilentLogger")



''' 可否增加一个监听广播的方法？ '''
# dev.startActivityWithParams(u"tel:10086", u"android.intent.action.DIAL",u"",u"",None,None,u"",0)



''' 为明白setWatcher调用方法'''
# dev.setSearchText(u"Camera", u"相机", None)
# dev.setWatcherSObject(u"Camera")
# for i in xrange(10):
#     print dev.waitForSObject(u"Camera", 2000)
# dev.setTestResult(True)


''' 为明白作用，是电量低出弹出的警告时，调用方法？'''
# global result
# result = False
# def Foo(x):
#     global result
#     if ("device: " in x) and ("battery level: " in x) :
#         result = True
#     
# dev.setBatteryTrackerCallableFunction(Foo)
# 
# dev.wake()
# dev.unlock()
# dev.home()
# for x in range(120) :
#     dev.sleep(500)
#     if result :
#         break





'''
1.需要setting list
2.可增加getPhoneSetting()?
3.有些设置，需要重启才能生效
'''
# dev.setPhoneSetting(u"screen_brightness", u"50")




''' 真的可以发mySingle邮件？'''
# print dev.sendMySingleMail( "yisheng.chen@samsung.com", "yisheng.chen@samsung.com", "STP Alert!",
#                       u"Very important logs!", ["1.png",])


# dev.setCOM("COM1")
# dev.setATCommand("AT")
# dev.releaseCOM()


''' 保存dumpstate到res目录下  '''
# dev.saveDumpState(u"dumpstate_one")


# dev.run(u"我的文件")


# dev.startActivity("com.android.mms/.ui.ConversationComposer")
# top = node.TopNode(dev)
# top.type(dev, "contacts", clean_before=True)


''' runner 这个类没有解释 , menu_tree_test? '''
# dev.setSearchText("1", "App notifications", 0)
# dev.setSearchText("2", "Auto check spelling", 0)
# dev.setSearchText("3", "User manual", 0)
# dev.setSearchText("4", "Wi-Fi", 0)
# dev.setSearchText("5", "Mobile hotspot and tethering", 0)
# dev.setSearchText("6", "VPN", 0)
# dev.setSearchText("7", "Enable as scheduledxxxxxxxxxxx", 0)
# dev.setSearchText("8", "Do not disturb", 0)
# dev.setSearchType("9", "com.sec.android.touchwiz.widget.TwTimePicker", 0)
# dev.setSearchText("10", "Ringtones and sounds", 0)
# dev.setSearchText("11", "Developer options", 0)
# dev.setSearchText("12", "Applications", 0)
# dev.setSearchText("13", "Backup and reset", 0)
# dev.setSearchText("14", "Download fonts", 0)
# dev.setSearchText("15", "Cancel", 0)
# dev.setSearchText("16", "Done", 0)
# dev.setSearchText("17", "Set as wallpaper", 0)
# dev.setSearchText("18", "Lock screen and security", 0)
# dev.setSearchText("19", "Add account", 0)
# dev.setSearchText("20", "Privacy", 0)
# dev.setSearchText("21", "Accounts", 0)
# dev.setSearchText("22", "Language", 0)
# dev.setSearchText("23", "Storage", 0)
# dev.setSearchText("24", "Text-to-speech options", 0)
# dev.setSearchText("25", "Add account", 0)
# dev.setSearchText("26", "Voice input", 0)
# dev.setSearchText("27", "Google voice typing", 0)
# dev.setSearchText("28", "Battery", 0)
# dev.setSearchType("29", "android.widget.DatePicker", 0)
# 
# exc_package = ["com.android.contacts", "com.android.vending"]
# excep_obj = map(str, range(1,30))
# #run = Runner(dev, [], exc_package)
# run = Runner(dev, excep_obj, exc_package)
# 
# print run.save_xls("/tmp/test.xls")
# dev.setTestResult(True)

''' 以下两个的区别 '''
# print dev.getTopScreen()
# print dev.getTopActivity()



''' ScreenDensity 是什么？ 密度，常见取值 1.5， 1.0 和标准dpi的比例（160px/inc）'''
# print "Now we use devices with screen density: %d" % dev.getScreenDensity()
# dim= dev.getScreenDimensions()
# print "Now we use devices with resolution: %d %d" % (dim.getHeight(), dim.getWidth())



# property_list = dev.getPropertyList()
# for l in list(property_list): 
#     value = dev.getProperty(l).encode("utf-8") 
#     print l, ":", value



''' 未清楚这里的node的定义， .+表示非空？ '''
# top = node.TopNode(dev)
# app_list = top.get_node_by_text(".+")
# for app in app_list:
#     print app


''' 没有说明  IDevicesManager 封装了什么方法？ '''
# devm = get_android_devices_manager()
# dev = get_selected_device()
# print devm.getOsString() # result: android




''' 直接调用会出现 wolfserver crash '''
# print dev.getLocation()


# dev.drag(159, 1287, 464, 1267, 200, 2000)
# dev.setTestResult(True)

# dev.startActivity(u"com.sec.android.app.sbrowser/.SBrowserMainActivity")
# dev.waitForActivity(u"com.sec.android.app.sbrowser/.SBrowserMainActivity", 3000)
# dev.setSearchObject(u"edit_text", u".*", u"android.widget.EditText", u".*", None)
# dev.waitForSObject(u"edit_text", 2000)
# dev.clickSObject(u"edit_text")
# dev.sleep(1000)
# # 使用了wolf server的输入法
# dev.type(u"")
''' type() 输入支持中文 '''
# # dev.type(u"中华人人民共和国")  
'''Type text using shell input text command'''
# dev.inputText(u"www.baidu.com") # 仅仅支持中文


# result = dev.debugBridgeCommand(u"version", 2000)
# print result.encode("utf-8")  # used to print result of debugBridgeCommand in console


# dev.addTextResult(u"AHOJ adventure!!! This is sample text result", True)
# dev.addTextResult(u"This is sample text result with False value", False)


# dev.statusbarOpenNotification()
# dev.statusbarOpenSettings()
# Write your code here
''' 保存一个字符内容 到项目文件中 '''
# dev.saveString("test.txt", "test string", "default text")

''' 保存输入法的 备选 区域为图片，到res目录 '''
# dev.saveKeyboardKeysImages()

# dev.inputText("test")

''' power 和 wake 区别？'''
# dev.power()
# dev.wake()

# result = False
#
''' 可抓取toast内容，但需要等待一定时间 '''
# def Foo(toast_text):
#     print toast_text.encode("utf-8")
#     global result
#     result = True
# 
# dev = get_selected_device()
# dev.setToastTrackerCallableFunction(Foo)
''' 向手机中发送toast功能 '''
# dev.sendAgentCommand(u"TOAST_LONG 中华人民共和国")

# for i in range(20):
#    dev.sleep(500)
#    if result:
#        break


# print dev.getDeviceId()
# print dev.getICCID()

''' 剪切板 功能 '''
# dev.setClipboard(u"中华人民共和国")
# print dev.getClipboard().encode("utf-8")

# agent_name = dev.getAgentName()  # return current name of stp agent
# print agent_name.encode("utf-8")


# dev.home()
# dev.call("10086")

''' TopNode 的用法和setSearch的区别？ click_on_text为什么还有传入dev?'''
# top = node.TopNode(dev)
# top.disp()
# top.click_on_text(u"陈", dev)

# print dev.API_LEVEL
# print dev.PATH
# print dev.SHORT_TIME_FOR_REINITIALIZATION

''' sendAgentCommand可以给wolfsever发指令，但是指令列表需要找HQ要 '''
# print dev.sendAgentCommand("TOAST_LONG TEST FIND")

# print dev.checkKeypad()
# print dev.dump().encode('utf-8')
# 
# print dev.dumpZ().encode('utf-8')

''' 读取某个号码的所有短信功能 '''
# lis = dev.fetchAllSmsMms("95313")
# 
# for m in lis:
#     print m.encode('utf-8')


