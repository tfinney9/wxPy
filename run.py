# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:41:02 2017

@author: tanner

File for a single windNinja Run
"""

#import os
#import subprocess32
#import zipfile
#import copy
import shutil
#import datetime
#import time
import glob
#import csv

#def getWxModelLocation():
#wZ=glob.glob('/home/tanner/src/wxPy/wxModel/')
#
#
#def writeWNcfg():
#    print "writing new cfg"
#    fout = open("/home/tanner/src/wxPy/A.cfg", 'w')
#    fout.write('num_threads                 =   4\n') #output not written in order for wx files if >1
#    fout.write('elevation_file              =   /home/tanner/src/wxPy/tif/greater-mso.tif\n')
#    fout.write('initialization_method       =   wxModelInitialization\n')
#    fout.write('time_zone                   =   America/Denver\n')
#    fout.write('forecast_filename           =   /home/tanner/src/wxPy/wxModel/wrfout_d01_2017-05-12_100000\n')
##    fout.write('forecast_duration               = 24\n')
#    fout.write('output_wind_height          =   10\n')
#    fout.write('units_output_wind_height    =   m\n')
##    fout.write('momentum_flag               =   true\n')
#    fout.write('vegetation                  =   trees\n')
##    fout.write('vegetation                  =   grass\n')
#    fout.write('mesh_resolution             =   690\n')
#    fout.write('units_mesh_resolution       =   m\n')
#    fout.write('write_goog_output           =   true\n')
#    fout.write('units_goog_out_resolution   =   m\n')
##    fout.write('diurnal_winds               =   true\n')
##    fout.write('non_neutral_stability       =   true\n')
#    fout.write('write_wx_model_goog_output  =   true\n')
#    fout.write('output_path                 =   /home/tanner/src/wxPy/out/')
##    if(initMethod == 'pointInitialization'):
##        fout.write('wx_station_filename         =   wxstation.csv\n')
##        fout.write('match_points                =   false\n')
##        fout.write('alpha_stability             =   %.2f\n' % alpha)
##    elif(initMethod == 'wxModelInitialization'):
##        fout.write('forecast_filename       =   %s\n' % wxFile)
#    fout.close()

#def runWN():
#    print "Running WindNinja... wxModelIni.py"
#    subprocess32.call(['/home/tanner/src/wind/build/src/cli/./WindNinja_cli',
#        '/home/tanner/src/wxPy/A.cfg'])

#def renameFiles():
#    print "renaming KMZs"
#    kmz=glob.glob('/home/tanner/src/wxPy/out/*.kmz')
#    os.rename(kmz[0],'/home/tanner/src/wnpy2/standard/pStandard.zip')
#    vel=glob.glob('/home/tanner/src/wnpy2/standard/*_vel.asc')
#    ang=glob.glob('/home/tanner/src/wnpy2/standard/*_ang.asc')
#    os.rename(vel[0],'/home/tanner/src/wnpy2/standard/data/velStandard.asc')
#    os.rename(ang[0],'/home/tanner/src/wnpy2/standard/data/angStandard.asc')
#

#writeWNcfg()
#runWN()

#kmz=glob.glob('/home/tanner/src/wxPy/out/*.kmz')


#os.rename(kmz[0],'/home/tanner/src/wxPy/out/*.zip')
#for i in range(len(kmz)):
#    os.rename(kmz[i],'/home/tanner/src/wxPy/out/*.zip')


def copyRunFiles():
    wrZ=glob.glob('/home/nwagenbrenner/nightly_wrf/output/ninjaout/*0.kmz')
    trZ=glob.glob('/home/nwagenbrenner/nightly_wrf/output/ninjaout/*m.kmz')
    for i in range(len(wrZ)):
        shutil.copyfile(wrZ[i],'/home/tfinney/wxPy/wxModel/'+wrZ[i][-31:])
#        print wrZ[i][-31:]
    for i in range(len(trZ)):
        shutil.copyfile(trZ[i],'/home/tfinney/wxPy/out/'+trZ[i][-28:])
#        print trZ[i][-28:]


#copyRunFiles()
