import arcpy

input_point = arcpy.GetParameterAsText(0)
evaluate_against_fc = arcpy.GetParameterAsText(1)
name_field = arcpy.GetParameterAsText(2)
name_value =arcpy.GetParameterAsText(3)
# checking that parameters are correct
arcpy.AddMessage(f"input_point {input_point}")
arcpy.AddMessage(f"Name field {name_field}")
arcpy.AddMessage(f"Name value {name_value}")
arcpy.AddMessage(f"evaluate_against_fc {evaluate_against_fc}")
# sql statement
sql = f"{name_field}='{name_value}'"
# make layer
arcpy.MakeFeatureLayer_management(in_features=evaluate_against_fc,out_layer='feature_near',where_clause=sql)

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