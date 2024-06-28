import arcpy

arcpy.env.overwriteOutput = True

# parameters
in_fc = r"C:\Users\PhilippeRieffel\Documents\Unikurs\arcpy_2\ArcGIS Pro Project\arcpy_2\arcpy_2.gdb\stops_ms_mitte"
out_fc = r"C:\Users\PhilippeRieffel\Documents\Unikurs\arcpy_2\ArcGIS Pro Project\arcpy_2\arcpy_2.gdb\stops_ms_mitte_buffered"
buffer_distance = "20 Meters"

arcpy.analysis.PairwiseBuffer(
    in_features=in_fc,
    out_feature_class=out_fc,
    buffer_distance_or_field=buffer_distance
)