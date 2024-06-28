import arcpy

point_for_test = arcpy.GetParameterAsText(0)
stops_ms_mitte = r"C:\Users\job02\Downloads\arcpy_2.gdb\arcpy_2.gdb\stops_ms_mitte"  # Hardcoded fc you should adjust the file location

arcpy.analysis.Near("point_for_test",
                    "stops_ms_mitte", None,
                    "LOCATION", "NO_ANGLE",
                    "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST;NEAR_X NEAR_X;NEAR_Y NEAR_Y")

fid = None
distance = None
bus_stop_name = None
input_cursor_fields = ['NEAR_FID','NEAR_DIST']
bus_fields = ['name','OBJECTID']

for row in arcpy.da.SearchCursor(in_table=point_for_test,field_names=input_cursor_fields):
    fid = row[0]
    distance = row[1]
    for bus_row in arcpy.da.SearchCursor(in_table=stops_ms_mitte ,field_names=bus_fields, where_clause=f"OBJECTID ={fid}"):
        bus_stop_name = bus_row[0]

arcpy.AddMessage(f"The nearest bus stop is '{bus_stop_name}' at a distance of {distance} meters.")
