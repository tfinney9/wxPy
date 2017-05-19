# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:27:57 2017

@author: tanner
"""

import os
import subprocess32
import zipfile
import copy
import shutil
import datetime
import time
import glob
import csv
import pathlib
import numpy

def extractKMZ():
    wrfZ=glob.glob('/home/tfinney/wxPy/wxModel/*.kmz')
    for i in range(len(wrfZ)):
        with zipfile.ZipFile(wrfZ[i],"r") as z:
            z.extractall('/home/tfinney/wxPy/wxModel/extract_wrf/')
def getKMLS():
    kZ=glob.glob('/home/tfinney/wxPy/wxModel/extract_wrf/*.kml')
    for i in range(len(kZ)):
        os.rename(kZ[i],'/home/tfinney/wxPy/wxModel/kml_wrf/'+kZ[i][-8:])

def moveKMLs():
    kZ=glob.glob('/home/tfinney/wxPy/wxModel/kml_wrf/*.kml')
    for i in range(len(kZ)):
        os.rename(kZ[i],'/home/tfinney/ninjaoutput/wrfSim/wrf/wrf_'+kZ[i][-8:])

def cleanDirs():
    kZ=glob.glob('/home/tfinney/wxPy/wxModel/*.kmz')
    for i in range(len(kZ)):
        os.remove(kZ[i])
    bZ=glob.glob('/home/tfinney/wxPy/wxModel/extract_wrf/*.bmp')
    for i in range(len(bZ)):
        os.remove(bZ[i])

def cleanTestDir():
    kZ=glob.glob("/home/tfinney/ninjaoutput/wrfSim/wrf/*")
    for i in range(len(kZ)):
        os.remove(kZ[i])
