# -*- coding: utf-8 -*-
from com.samsung.stp.engine.TouchPressType import *
from stp_lib.devices import get_selected_device

from jxl import Workbook
from jxl import Sheet
from jxl import Cell
from jxl.write import Label
from java.io import File
from stp_lib.project import Project
import sys, os, time

path = Project.get_absolute_res_path() + "\excel.xls"

def createWB():
    
    wb = Workbook.createWorkbook(File(path))
    sheet = wb.createSheet(u"产品清单", 0)
    label = Label(0, 0, "test")
    sheet.addCell(label)
    wb.write();
    wb.close();

def readWB():
    wb = Workbook.getWorkbook(File(path))
    sheet = wb.getSheet(0)
    print sheet.getName().encode("utf-8")

start = time.time()
# print Project.get_absolute_path()
createWB()
readWB()

print int(((3880) % 3600)/60)
# pwd = sys.path[0]
# print os.path.abspath(os.path.join(pwd, os.pardir, os.pardir))
print "end"

