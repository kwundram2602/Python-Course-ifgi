# Modify this file to be used with arcpy.GetParametersAsText(0) and arcpy.AddMessage()

import arcpy, sys

arcpy.env.overwriteOutput = True

# parameters
in_fc = arcpy.GetParameterAsText(0)
name_field = arcpy.GetParameterAsText(1)
name_value = arcpy.GetParameterAsText(2)
out_fc = arcpy.GetParameterAsText(3)
buffer_distance = arcpy.GetParameterAsText(4)

# checking that parameters are correct
arcpy.AddMessage(f"Input Path {in_fc}")
arcpy.AddMessage(f"Name field {name_field}")
arcpy.AddMessage(f"Name value {name_value}")
arcpy.AddMessage(f"Output Path {out_fc}")
arcpy.AddMessage(f"Buffer Distance {buffer_distance}")

# Build a layer with the name field & field value
sql = f"{name_field}='{name_value}'"
arcpy.AddMessage(f"SQL Clause {sql}")
arcpy.MakeFeatureLayer_management(in_features=in_fc,out_layer='feats_to_buffer',where_clause=sql)

# run work
arcpy.analysis.PairwiseBuffer(
    in_features='feats_to_buffer',
    out_feature_class=out_fc,
    buffer_distance_or_field=buffer_distance
)

arcpy.AddMessage('Work Done')