# coding: utf-8
import arcpy
import os
db = r"D:\ArcGIS\Py_Arc\exercise_arcpy_1.gdb"
arcpy.env.workspace =db

# all point features
point_featureClasses = arcpy.ListFeatureClasses(feature_type="Point")
# status of feature
cursor_fields = ['Shape@XY','status','type']
# delete active assets from point features so no features are copied twice
point_featureClasses = [x for x in point_featureClasses if x != 'active_assets']
print("point_featureClasses", point_featureClasses)

# active assets
active_assets_fc ='active_assets'
active_assets_path= os.path.join(arcpy.env.workspace,active_assets_fc)
print("active_assets_path",active_assets_path)

# insert into active assets
icur = arcpy.da.InsertCursor(in_table=active_assets_path,field_names=cursor_fields)

# iterate point features
for point_fc in point_featureClasses:
    # feature path
    fc_path = os.path.join(arcpy.env.workspace,point_fc)
    # get status of each feature
    for row in arcpy.da.SearchCursor(in_table=fc_path,field_names=cursor_fields):
        status = row[1]
        #print(row)
        #print(point_fc,str(status))
        if status =='active':
            #print("is active")
            icur.insertRow(row)
del icur