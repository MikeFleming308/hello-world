
#---------------------------------------------------------------------------
#
# ClipImageByRectangle.py
# Mike Fleming mcfleming@goldcoast.qld.gov.au
# Created: 07/02/2017
# Last updated 07/02/2017
# Description: 
# Requirements: Spatial Analyst Extension
#
#---------------------------------------------------------------------------

# Setup status output
scriptName = 'ClipImageByRectangle.py'
StartTime = time.strftime("%#c", time.localtime())
startText = "____________________Script started successfully.____________________"
arcpy.AddMessage(" " * 3)
arcpy.AddMessage("         -<>-<>-<>-" * 3)
arcpy.AddMessage(" ")
arcpy.AddMessage(startText)
arcpy.AddMessage("\n")
arcpy.AddMessage(StartTime)


# Import system modules
import arcpy, time, os
from arcpy import env
from arcpy.sa import *


# User-supplied parameters
inRasterDir = arcpy.GetParameterAsText(0)
llx = arcpy.GetParameterAsText(1)
lly = arcpy.GetParameterAsText(2)
urx = arcpy.GetParameterAsText(3)
ury = arcpy.GetParameterAsText(4)

# Set environment settings
env.workspace = inRasterDir


# Set local variables
inRectangle = Extent(llx, lly, urx, ury)
clipd = "Clipped"
outPath = os.path.join(inRasterDir, clipd)
counter = 0

msg = "\nChecking if output folder exists..."
arcpy.AddMessage(msg)

if not os.path.isdir(outPath):
    msg = "\nCreating output folder..."
    arcpy.AddMessage(msg)
    os.mkdir(outPath)
rasterList = arcpy.ListFiles("*.tif*")
msg = "\nOutput *.tiff files will be written to: " + outPath
arcpy.AddMessage(msg)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractByRectangle in for loop
for r in rasterList:
    counter += 1
    pnum = r.split(".")[0][-2:]
    clipdraster = ExtractByRectangle(r, inRectangle, "INSIDE")
    # Save the output
    fName = "Page_{}_Map_{}.tif".format(pnum, str(counter))
    outFPath = os.path.join(outPath, fName)
    msg = "\nCreating " + fName
    arcpy.AddMessage(msg)
    clipdraster.save(outFPath)


# Final status output
arcpy.AddMessage("\nStarted  " + scriptName)
arcpy.AddMessage(StartTime)
arcpy.AddMessage("\nFinished " + scriptName)
finishTime = time.strftime("%#c", time.localtime())
arcpy.AddMessage(finishTime)
arcpy.AddMessage("\n=====================================================================")







