# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:44:15 2017

@author: tanner
"""

import os
#import subprocess32
import zipfile
import copy
import shutil
import datetime
import time
import glob
import csv
import pathlib
import numpy

zDir="/home/tfinney/wxPy/zip_out/"
kDir="/home/tfinney/wxPy/kml_out/"
vecDir="/home/tfinney/wxPy/overwrite/kml/"
dateDir="/home/tfinney/wxPy/overwrite/datetime/"
bmpDir="/home/tfinney/wxPy/overwrite/key/"


def createZip():
    kmz=glob.glob('/home/tfinney/wxPy/out/*.kmz')

    for i in range(len(kmz)):
        basePath=pathlib.Path(kmz[i]).stem+".zip"
        pathDir=zDir+basePath
        os.rename(kmz[i],pathDir)

def extractZip():
    zZ=glob.glob('/home/tfinney/wxPy/zip_out/*.zip')
    for i in range(len(zZ)):
        with zipfile.ZipFile(zZ[i],"r") as z:
            z.extractall(kDir)

#bmpTime=glob.glob('/home/tanner/src/wxPy/kml_out/*.date_time.bmp')
#bmpKey=glob.glob('/home/tanner/src/wxPy/kml_out/*stability.bmp')
#kml=glob.glob('/home/tanner/src/wxPy/kml_out/*.kml')
#
#kml.sort()
#bmpTime.sort()
#bmpKey.sort()

#simTimes=['0500','0600','0700','0800','0900','1000',
#'1100','1200','1300','1400','1500','1600',
#'1700','1800','1900','2000','2100','2200',
#'2300','0000','0100','0200','0300','0400']

def sortFiles():
    bmpTime=glob.glob('/home/tfinney/wxPy/kml_out/*.date_time.bmp')
    bmpKey=glob.glob('/home/tfinney/wxPy/kml_out/*m.bmp')
    kml=glob.glob('/home/tfinney/wxPy/kml_out/*.kml')
    kml.sort()
    bmpTime.sort()
    bmpKey.sort()
    for i in range(len(kml)):
        kmlName=vecDir+kml[i][42:46]+".kml"
        dateName=dateDir+bmpTime[i][42:46]+".date_time.bmp"
        bmpName=bmpDir+bmpKey[i][42:46]+".key.bmp"
        os.rename(kml[i],kmlName)
        os.rename(bmpTime[i],dateName)
        os.rename(bmpKey[i],bmpName)

def removeZips():
    zZ=glob.glob('/home/tfinney/wxPy/zip_out/*.zip')
    for i in range(len(zZ)):
        os.remove(zZ[i])

def cleanOverwrite():
    vZ=glob.glob("/home/tfinney/wxPy/overwrite/kml/*")
    dZ=glob.glob("/home/tfinney/wxPy/overwrite/datetime/*")
    bZ=glob.glob("/home/tfinney/wxPy/overwrite/key/*")
    for i in range(len(vZ)):
        os.remove(vZ[i])
        os.remove(dZ[i])
        os.remove(bZ[i])

def cleanTestDir():
    kZ=glob.glob("/home/tfinney/ninjaoutput/wrfSim/kml/*")
    for i in range(len(kZ)):
        os.remove(kZ[i])

def cleanKMZDir():
    kmz=glob.glob('/home/tfinney/wxPy/out/*.kmz')
    for i in range(len(kmz)):
        os.remove(kmz[i])

def writeLogFile():
    print "writing logFile..."
    log=open('/home/tfinney/wxPy/wxLog.txt','w')
    log.write('High-resolution WRF\n')
    log.write('All timesteps are in local time. ')
    log.write('Simulation valid for: ')
    log.write(str(datetime.datetime.now())[:-16])
    log.close()

def moveToTestDir():
    kZ=glob.glob("/home/tfinney/wxPy/overwrite/kml/*")
    for i in range(len(kZ)):
        shutil.copyfile(kZ[i],"/home/tfinney/ninjaoutput/wrfSim/kml/"+kZ[i][-8:])

def moveLogFile():
    shutil.copyfile('/home/tfinney/wxPy/wxLog.txt','/home/tfinney/ninjaoutput/wrfSim/wxLog.txt')




#dloc="/home/tanner/src/wxPy/demo/big_butte_09-05-2010_0500_690m_non_neutral_stability.kmz"
#base="/home/tanner/src/wxPy/demo/"
#nloc=pathlib.Path(dloc).stem+".zip"
#floc=base+nloc
#os.rename(dloc,floc)

#os.rename(kmz[0],'/home/tanner/src/wxPy/out/*.zip')
#for i in range(len(kmz)):
#    os.rename(kmz[i],'/home/tanner/src/wxPy/out/*.zip')
