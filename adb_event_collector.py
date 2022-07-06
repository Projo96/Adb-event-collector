#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os
#from PIL import Image, ImageStat
from multiprocessing import Process
from utils.adbclient import AdbClient
from threading import *
from time import *
from sys import platform
import ctypes
PORT = 5555

adb_path = '.'
output_path = './collected_data/'

if len(sys.argv) >= 2:
    serialno = sys.argv[1]
else:
    serialno = '.*'


class save_touch(Thread):
    def run(self):
        adbclient = AdbClient(serialno=serialno,)
        adbclient.shell('getevent -lrt',output_file=output_path+'touch.txt')



class save_accessibility(Thread):
    def run(self):
        adbclient = AdbClient(serialno=serialno)
        adbclient.shell('uiautomator events',output_file=output_path+'access.txt')


def verifyIfNotConnected(adbDevices, ip):
    # Verify if the device is already connected (wifi)
    return adbDevices.find(ip) == -1

def connectToDevice(ip):
    # Connect to an android device
    print('Accept prompt one last time')
    
    os.popen("adb connect " + ip + ":" + str(PORT)).read()
    #sleep(3)
    input("press any key when you're done")
    ip_addr = getIP()
    if ip_addr == ip:
        return True
    else:
        return False


def getDecidesIDs(adbDevices):
    # Get all device IDs connected in an USB port
    return re.findall('(.*?)\tdevice', adbDevices)


def getIP():
    # Find ip from the device connect in USB port--> togliere il grep e mettere adb shell ip addr show wlan0
    
    net_stats= os.popen("adb shell ip addr show wlan0").read().rstrip()
    ip_addr = re.findall( r'[0-9]+(?:\.[0-9]+){3}', net_stats )[0]
    
    if ip_addr != '':
        print('Device Detected')
        return ip_addr
    else:
        raise Exception("Sorry, no device detected")
    

def adbOverWiFi():
   
    os.popen("adb kill-server")
    print('Accept promtp on the screen')
    #os.chdir(adb_path)
    adbDevices = os.popen("adb start-server").read()#start the adb client need to be in the same dir as adb.exe
    #sleep(5)#wait for user to interact
    #Mbox('Test', 'Accept prompt on the screen', 0)
    #input("press any key when you're done")
    try:
      
        #if deviceID != '':
           # print('Device Detected')
        #else:
            #raise Exception("Sorry, no device detected")
        ip_addr = getIP()
        #os.chdir(adb_path)
        os.popen("adb tcpip " + str(PORT))
        print("PORT 5555 open for " + ip_addr)
        print('Disconnect device from the cable')
        input("press any key when you're done")#sleep(4) # Sleep for 3 seconds

        if (connectToDevice(ip_addr)):
            print("Connected to " + ip_addr)
        else:
            print("Failed to connected to " + ip_addr)
    except:
        if getIP() != None:
            print('Device connected but error')
        else:
            print('ERROR')

def saveDeviceDisplayInfo(path):#to be called after the device is connected
    adbclient = AdbClient(serialno=serialno,)
    #info = adbclient.getPhysicalDisplayInfo()
    screen_info = adbclient.getDisplayInfo()
    #info3 = adbclient.getLogicalDisplayInfo()
    #print(info,info2,info3)


    f = open(path+'screen.txt', 'a')
    f.write(str(screen_info))
    f.close()
    return 

def define_adb_path():
    global adb_path
    global output_path
    if platform == "linux" or platform == "linux2":
        # linux
        adb_path = './platform-tools_linux/'
    elif platform == "darwin":
        # OS X
        adb_path = './platform-tools_darwin/'
    elif platform == "win32":
        # Windows..
        
        adb_path ='./platform-tools_win32/'
        output_path = os.getcwd()+'\\collected_data\\'

#adbclient1 = AdbClient(serialno=serialno)

#adbclient1.shell('getevent -lrt')
#adbclient1.shell('uiautomator events')
#adbclient1.shell('ip addr show wlan0',customTest=True)
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#MAIN CODE  
define_adb_path()  
os.chdir(adb_path)
adbOverWiFi()
saveDeviceDisplayInfo(output_path)


app1 = save_touch()
app2 = save_accessibility()

print('Start Collecting Data')
app1.start()
app2.start()

app1.join()
app2.join()
