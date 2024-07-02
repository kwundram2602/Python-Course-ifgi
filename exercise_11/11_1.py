import arcpy
import time

# add Progressor
arcpy.SetProgressor(type='step',message='Progress in my Script',min_range=0, max_range=3,step_value=1)

# add first progressor position
arcpy.SetProgressorLabel("Checking the inputs")
arcpy.SetProgressorPosition(0)

input_point = arcpy.GetParameterAsText(0)
evaluate_against_fc = arcpy.GetParameterAsText(1)
name_field = arcpy.GetParameterAsText(2)
name_value =arcpy.GetParameterAsText(3
                                     )
# checking that parameters are correct
arcpy.AddMessage(f"input_point {input_point}")
arcpy.AddMessage(f"Name field {name_field}")
arcpy.AddMessage(f"Name value {name_value}")
arcpy.AddMessage(f"evaluate_against_fc {evaluate_against_fc}")

# set a break for two seconds
time.sleep(2)

# add second progressor position
arcpy.SetProgressorLabel("Building SQL")
arcpy.SetProgressorPosition(1)

# sql statement
sql = f"{name_field}='{name_value}'"

# set a break for two seconds
time.sleep(2)

# add third progressor position
arcpy.SetProgressorLabel("Create Layer")
arcpy.SetProgressorPosition(2)

# make layer
arcpy.MakeFeatureLayer_management(in_features=evaluate_against_fc,out_layer='feature_near',where_clause=sql)

# set a break for two seconds
time.sleep(2)

# add final progressor position
arcpy.SetProgressorLabel("Starting near tool")
arcpy.SetProgressorPosition(3)
# near tool
arcpy.analysis.Near(input_point,
                    'feature_near', None,
                    "LOCATION", "NO_ANGLE",
                    "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST;NEAR_X NEAR_X;NEAR_Y NEAR_Y")

fid = None
distance = None
bus_stop_name = None
input_cursor_fields = ['NEAR_FID','NEAR_DIST']
bus_fields = ['name','OBJECTID']

for row in arcpy.da.SearchCursor(in_table=input_point,field_names=input_cursor_fields):
    fid = row[0]
    distance = row[1]
    for bus_row in arcpy.da.SearchCursor(in_table=evaluate_against_fc ,field_names=bus_fields, where_clause=f"OBJECTID ={fid}"):
        bus_stop_name = bus_row[0]

arcpy.AddMessage(f"The feature '{bus_stop_name}' is {distance} meters away from the input point.")

time.sleep(2)
