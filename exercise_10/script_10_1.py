import arcpy
import sys
import os


arcpy.env.overwriteOutput = True

input_fc = arcpy.GetParameterAsText(0)
db = r"D:\ArcGIS\Py_Arc\arcpy_2.gdb"
# db = arcpy.GetParameterAsText(1)

# Near tool change first paramter to input_fc
arcpy.analysis.Near("point_for_test",
                    "stops_ms_mitte", None,
                    "LOCATION", "NO_ANGLE",
                    "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST;NEAR_X NEAR_X;NEAR_Y NEAR_Y")

# workspace
arcpy.env.workspace =db

# input feature class path # change later to get paramter
input_path = os.path.join(arcpy.env.workspace,"point_for_test")

# bus stop feature class path 
bus_path = os.path.join(arcpy.env.workspace,"stops_ms_mitte")

#  search in input for fif and distance
input_cursor_fields = ['NEAR_FID','NEAR_DIST']
bus_fields = ['name','OBJECTID']
for row in arcpy.da.SearchCursor(in_table=input_path,field_names=input_cursor_fields):
    #print("row[0]:",row[0])
    #print("row[1]:",row[1])
    fid = row[0]
    distance = row[1]
    for bus_row in arcpy.da.SearchCursor(in_table=bus_path,field_names=bus_fields, where_clause=f"OBJECTID ={fid}"):
        #print("row[0] bus:",bus_row[0])
        #print("row[1] bus:",bus_row[1])
        bus_stop_name = bus_row[0]