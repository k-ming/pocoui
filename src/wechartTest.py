# -*- coding: utf-8 -*-#
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android import Android
import time
import os
3  #------------------------------------
4  # Name:         wechartTest
5  # Description:  
6  # Author:       kingming
7  # Date:         2020/5/25
8  #------------------------------------

android = Android
print 'start...'
poco = AndroidUiautomationPoco()
screenWidth,screenHeigth = poco.get_screen_size()
poco.device.wake()
start_app("com.tencent.mm")
poco("com.tencent.mm:id/f4u").wait_for_appearance(15)
poco("com.tencent.mm:id/f4u").click()
poco("com.tencent.mm:id/bfl").wait_for_appearance(15)
poco("com.tencent.mm:id/bfl").click()
text('weixinyundong')
poco("com.tencent.mm:id/f5h").offspring("com.tencent.mm:id/f50")[1].click()
poco("com.tencent.mm:id/aks").click()
def getZan():
    return poco("com.tencent.mm:id/bn2").offspring("com.tencent.mm:id/bm7")
for i in range(1, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)

swipe((screenWidth*0.5, screenHeigth*0.9), vector=[0, -0.85], duration=3)
for i in range(0, len(getZan())-1):
    getZan()[i].click()
time.sleep(2)