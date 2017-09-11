"""
Created on Thu May 11 08:44:15 2017

@author: tanner
"""
import glob
import os

def getKeys():
    print 'Moving Keys...'
    wZ=glob.glob('/home/tfinney/wxPy/wxModel/extract_wrf/*0.bmp')
    kZ=glob.glob('/home/tfinney/wxPy/overwrite/key/*.bmp')
    for i in range(len(wZ)):
        os.rename(wZ[i],'/home/tfinney/ninjaoutput/wrfSim/wrf_key/'+wZ[i][62:])
    for i in range(len(kZ)):
        os.rename(kZ[i],'/home/tfinney/ninjaoutput/wrfSim/kml_key/'+kZ[i][33:])
