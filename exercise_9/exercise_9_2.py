import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"C:\Users\job02\Downloads\exercise_arcpy_1_neu.gdb\exercise_arcpy_1.gdb"

coverage_feature_class = "coverage"
input_feature_class = "active_assets"
helper_field = "buffer_dist"

buffer_dist = {"mast": 300, 
               "mobile_antenna": 50, 
               "building_antenna": 100}

arcpy.management.AddField(input_feature_class, helper_field, "FLOAT")

cursor = arcpy.da.UpdateCursor(input_feature_class, ["type", helper_field])

for row in cursor:
    type = row[0]
    if type in buffer_dist:
        row[1] = buffer_dist[type]
    else:
        row[1] = None
    cursor.updateRow(row)

del cursor

arcpy.analysis.Buffer(input_feature_class, coverage_feature_class, helper_field)

if helper_field in [field.name for field in arcpy.ListFields(input_feature_class)]:
    arcpy.DeleteField_management(input_feature_class, helper_field)