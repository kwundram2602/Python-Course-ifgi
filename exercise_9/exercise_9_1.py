# coding: utf-8
import arcpy
import os
db = r"D:\ArcGIS\Py_Arc\exercise_arcpy_1.gdb"
arcpy.env.workspace =db

point_featureClasses = arcpy.ListFeatureClasses(feature_type="Point")
cursor_fields = ['status']

# active assets
active_assets_path= os.path.join(arcpy.env.workspace,"active_assets")
# insert into active assets
icur = arcpy.da.InsertCursor(in_table=active_assets_path,field_names=cursor_fields)

for point_fc in point_featureClasses:
    fc_path = os.path.join(arcpy.env.workspace,point_fc)
    for status in arcpy.da.SearchCursor(in_table=fc_path,field_names=cursor_fields):
        
        print(status)