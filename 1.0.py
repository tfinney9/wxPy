#!/usr/bin/env python

import run
import modify
import writeJS
import wrf_modify
import moveKeys

#print "Writing Config..."
#run.writeWNcfg()

#print "Running WindNinja..."
#run.runWN()

print "Cleaing Directories..."
wrf_modify.cleanDirs()
modify.cleanKMZDir()

wrf_modify.cleanTestDir()
modify.removeZips()
modify.cleanTestDir()
modify.cleanOverwrite()

print "Copying Run Files..."
run.copyRunFiles()

print "Converting KMZ to Zip..."
modify.createZip()

print "Extracting Files from Zip..."
modify.extractZip()

print "Sorting Files..."
modify.sortFiles()

print "Moving files to AWS..."
modify.moveToTestDir()
modify.writeLogFile()
modify.moveLogFile()

print "moving WRF Files..."
wrf_modify.extractKMZ()
wrf_modify.getKMLS()
wrf_modify.moveKMLs()

print "Moving Keys..."
moveKeys.getKeys()

print "creating html..."
writeJS.makeHTMLFile()
writeJS.moveToTestLocation()
