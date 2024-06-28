# Modify this file to be used with arcpy.GetParametersAsText(0) and arcpy.AddMessage()

import arcpy, sys

arcpy.env.overwriteOutput = True

# parameters
in_fc = arcpy.GetParameterAsText(0)
out_fc = arcpy.GetParameterAsText(1)
buffer_distance = arcpy.GetParameterAsText(2)

# checking that parameters are correct
print(f"Input Path {in_fc}")
print(f"Output Path {out_fc}")
print(f"Buffer Distance {buffer_distance}")

# run work
arcpy.analysis.PairwiseBuffer(
    in_features=in_fc,
    out_feature_class=out_fc,
    buffer_distance_or_field=buffer_distance
)

print('Work Done')