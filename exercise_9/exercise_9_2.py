import arcpy

arcpy.env.overwriteOutput = True

# set workspace (change to your geodatabase)
arcpy.env.workspace = r"C:\Users\job02\Downloads\exercise_arcpy_1_neu.gdb\exercise_arcpy_1.gdb"

coverage_feature_class = "coverage"
coverage_feature_class = arcpy.ValidateTableName(coverage_feature_class)
input_feature_class = "active_assets"
input_feature_class = arcpy.ValidateTableName(input_feature_class)
helper_field = "buffer_dist"
helper_field = arcpy.ValidateFieldName(helper_field)

# set buffer distances
buffer_distances = {
    'mast': 300,
    'mobile_antenna': 50,
    'building_antenna': 100
}

# check if the helper field exists
field_names = [field.name for field in arcpy.ListFields(input_feature_class)]

# add helper field if its not existing else delete the existing one
if helper_field not in field_names:
    arcpy.management.AddField(input_feature_class, helper_field, "FLOAT")
else:
    arcpy.management.DeleteField(input_feature_class, helper_field)

# update the helper field with the corresponding distances
with arcpy.da.UpdateCursor(input_feature_class, ["type", helper_field]) as cursor:
    for row in cursor:
        asset_type = row[0]  
        if asset_type in buffer_distances:
            row[1] = buffer_distances[asset_type]
        else:
            row[1] = None  
        cursor.updateRow(row)

# create buffer 
arcpy.analysis.Buffer(input_feature_class, coverage_feature_class, helper_field)

print("Done")