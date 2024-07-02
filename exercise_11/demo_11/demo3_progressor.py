# Run the tool with copy/paste parameters for name_field & name_value first, then 
# use the validation_toolclass.py to build 

import arcpy, sys, time

arcpy.env.overwriteOutput = True

# parameters
in_fc = arcpy.GetParameterAsText(0)
name_field = arcpy.GetParameterAsText(1)
name_value = arcpy.GetParameterAsText(2)
out_fc = arcpy.GetParameterAsText(3)
buffer_distance = arcpy.GetParameterAsText(4)

# adding the progressor
#arcpy.SetProgressor(type='step',message='Progress in my Script',min_range=0, max_range=3,step_value=1)
#time.sleep(0.5)
# checking that parameters are correct
#arcpy.SetProgressorLabel("Checking the inputs")
#arcpy.SetProgressorPosition(0)
#time.sleep(2)
arcpy.AddMessage(f"Input Path {in_fc}")
arcpy.AddMessage(f"Name field {name_field}")
arcpy.AddMessage(f"Name value {name_value}")
arcpy.AddMessage(f"Output Path {out_fc}")
arcpy.AddMessage(f"Buffer Distance {buffer_distance}")

# Build a layer with the name field & field value
#arcpy.SetProgressorLabel("Building SQL")
#arcpy.SetProgressorPosition(1)
#time.sleep(2)
sql = f"{name_field}='{name_value}'"
arcpy.AddMessage(f"SQL Clause {sql}")
arcpy.MakeFeatureLayer_management(in_features=in_fc,out_layer='feats_to_buffer',where_clause=sql)

# run work
#arcpy.SetProgressorLabel("Runnning the Buffer")
#arcpy.SetProgressorPosition(2)
#time.sleep(2)

arcpy.analysis.PairwiseBuffer(
    in_features='feats_to_buffer',
    out_feature_class=out_fc,
    buffer_distance_or_field=buffer_distance
)

arcpy.AddMessage('Work Done')