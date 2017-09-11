# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:52:28 2017

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
import jsStyles

def getKmlList():
    kmlList=[]
    kZ=glob.glob("/home/tfinney/ninjaoutput/wrfSim/kml/*")
    for i in range(len(kZ)):
        keyhole=kZ[i][-8:]
        kmlList.append(keyhole)
    kmlList.sort()
    return kmlList

def writeFile(js):
    jOut=open('/home/tfinney/wxPy/display/wrf.html','w')
    jOut.write(js)
    jOut.close()

jsStart="""<div class="col col-6">
<!-- <h1 style="color:black;">A</h1> -->
<html>
<head>
<title>WRF WindNinja </title>
<style>
   html { height: 100%; }
   body { height: 100%; margin: 0; padding: 0; }
   #map_canvas { height: 100%; }
   #checkboxes {
  	position: absolute;
  	top: 70px;
  	right: 100px;
  	font-family: 'arial', 'sans-serif';
  	font-size: 14px;
  	background-color: white;
  	border: 1px solid gray;
  	padding: 5px 10px;
   }
   #wrfCheckBoxes {
   position: absolute;
   top: 70px;
   right: 10px;
   font-family: 'arial', 'sans-serif';
   font-size: 14px;
   background-color: white;
   border: 1px solid gray;
   padding: 5px 10px;
   }
   #infobox{
     position: absolute;
     top: 1px;
     right: 10px;
     font-family: 'arial', 'sans-serif';
     font-size: 14px;
     background-color: white;
     border: 1px solid gray;
     padding: 0px 0px;
   }

    }
</style>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false&key=AIzaSyBL2JbHu9cN3mSvKDvi_VPDQJHPwT2_w8M"></script>
<script type="text/javascript">
// Source: http://www.geocodezip.com/insight-projects_com_pedc_A.html

var map;
var layers = [];
var myCenter=new google.maps.LatLng(46.9163056,-114.0905556);

  function initialize() {
    // var myLatLng = new google.maps.LatLng(46.9163056,-114.0905556);
    var myOptions = {
      zoom: 10,
      center: myCenter,
      mapTypeId: google.maps.MapTypeId.TERRAIN,
      styles:
      [{"elementType": "geometry","stylers": [{"color": "#ebe3cd"}]},{"elementType": "labels.text.fill","stylers": [{"color": "#523735"}]},{"elementType": "labels.text.stroke","stylers": [{"color": "#f5f1e6"}]},{"featureType": "administrative","elementType": "geometry.stroke","stylers": [{"color": "#c9b2a6"}]},{"featureType": "administrative.land_parcel","elementType": "geometry.stroke","stylers": [{"color": "#dcd2be"}]},{"featureType": "administrative.land_parcel","elementType": "labels.text.fill","stylers": [{"color": "#ae9e90"}]},{"featureType": "landscape.natural","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "landscape.natural","elementType": "geometry.fill","stylers": [{"color": "#c2ce89"}]},{"featureType": "poi","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "poi","elementType": "labels.text.fill","stylers": [{"color": "#93817c"}]},{"featureType": "poi.park","elementType": "geometry.fill","stylers": [{"color": "#a5b076"}]},{"featureType": "poi.park","elementType": "labels.text.fill","stylers": [{"color": "#447530"}]},{"featureType": "road","elementType": "geometry","stylers": [{"color": "#f5f1e6"}]},{"featureType": "road.arterial","elementType": "geometry","stylers": [{"color": "#fdfcf8"}]},{"featureType": "road.highway","elementType": "geometry","stylers": [{"color": "#f8c967"}]},{"featureType": "road.highway","elementType": "geometry.stroke","stylers": [{"color": "#e9bc62"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry","stylers": [{"color": "#e98d58"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry.stroke","stylers": [{"color": "#db8555"}]},{"featureType": "road.local","elementType": "labels.text.fill","stylers": [{"color": "#806b63"}]},{"featureType": "transit.line","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "transit.line","elementType": "labels.text.fill","stylers": [{"color": "#8f7d77"}]},{"featureType": "transit.line","elementType": "labels.text.stroke","stylers": [{"color": "#ebe3cd"}]},{"featureType": "transit.station","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "water","elementType": "geometry.fill","stylers": [{"color": "#31404d"}]},{"featureType": "water","elementType": "labels.text.fill","stylers": [{"color": "#92998d"}]}]


    }
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
"""

jsMiddle="""for (var i = 0; i < layers.length; i++) {
        layers[i].setMap(null);
      }
  }

function toggleLayer(i) {
  if (layers[i].getMap() === null) {
    layers[i].setMap(map);
  }
  else {
    layers[i].setMap(null);
  }
}

</script>
</head>

<body onload="initialize()">
<div id="map_canvas"></div>
<div id="checkboxes">
  </>WindNinja<br />
"""
jsMid2="""</div>
<div id="wrfCheckBoxes">
  </>WRF<br />
"""
jsMid3="""</div>
<div id="infobox">"""
jsEnd="""</div>
</body>

</html>
</div>
"""

testLayer1="    layers [0] = new google.maps.KmlLayer('https://tfinney9.github.io/trombones/wx/kml/0000.kml',"
testLayer2="    {preserveViewport: false, suppressInfoWindows: false});"
testCheckbox="  <input type=\"checkbox\" id=\"layer0\" onClick=\"toggleLayer(0)\"/>0000 <br />"

path='http://windninja.wfmrda.org/ninjadata/'
logPath='http://windninja.wfmrda.org/ninjadata/wxLog.txt'

wrfPath='http://windninja.wfmrda.org/ninjadata/'


def makeLayer(num,address,name):
    lay1="    layers ["+str(num)+"]= new google.maps.KmlLayer('"+str(address)+str(name)+"',\n"
    lay2="    {preserveViewport: false, suppressInfoWindows: false});\n"
    return lay1+lay2

def makeCheckbox(num,name):
    cB="  <input type=\"checkbox\" id=\"layer"+str(num)+"\" onClick=\"toggleLayer("+str(num)+")\"/>"+str(name)+" <br />\n"
    return cB

def makeIFRAME(iframe_path):
    frame="<iframe src=\""+str(iframe_path)+"\" style=\"background: #FFFFFF;\" height=\"60\"  width=\"600\"></iframe>\n"
    return frame





def makeHTMLFile():
    kmlNames=getKmlList()
    kmlRange=numpy.arange(0,len(kmlNames))
#   layerList=[]
    layerstr=str()
    for i in range(len(kmlNames)):
        unLayer=makeLayer(kmlRange[i],path,kmlNames[i])
    #    layerList.append(unLayer)
        layerstr=layerstr+unLayer

#    checkList=[]
    checkstr=str()
    for i in range(len(kmlNames)):
        unCheck=makeCheckbox(kmlRange[i],kmlNames[i][:4])
    #    checkList.append(unCheck)
        checkstr=checkstr+unCheck

    wrfNames=getKmlList()
    wrfRange=numpy.arange(kmlRange[-1]+1,kmlRange[-1]+len(kmlRange)+1)

    for k in range(len(wrfNames)):
        wrfNames[k]="wrf"+wrfNames[k]

    wrfLayerstr=str()
    for i in range(len(wrfNames)):
        unWrfLayer=makeLayer(wrfRange[i],wrfPath,wrfNames[i])
        wrfLayerstr=wrfLayerstr+unWrfLayer
    wrfCheckstr=str()
    for i in range(len(wrfNames)):
        unWrfCheck=makeCheckbox(wrfRange[i],kmlNames[i][:4])
        wrfCheckstr=wrfCheckstr+unWrfCheck

    istr=makeIFRAME(logPath)
    jsFull=jsStart+layerstr+wrfLayerstr+jsMiddle+checkstr+jsMid2+wrfCheckstr+jsMid3+istr+jsEnd
    writeFile(jsFull)

def moveToTestLocation():
#    shutil.copyfile('/home/tanner/src/wxPy/display/wrf.html','/home/tanner/wnwebsrc/local/_posts/2017-05-17-wrfSim.html')
    shutil.copyfile('/home/tfinney/wxPy/display/wrf.html','/home/tfinney/ninjaoutput/wrfSim/wrf.html')
