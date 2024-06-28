import arcpy

arcpy.env.overwriteOutput = True

arcpy.analysis.PairwiseBuffer(
    in_features=r"C:\Users\PhilippeRieffel\Documents\Unikurs\arcpy_2\ArcGIS Pro Project\arcpy_2\arcpy_2.gdb\stops_ms_mitte",
    out_feature_class=r"C:\Users\PhilippeRieffel\Documents\Unikurs\arcpy_2\ArcGIS Pro Project\arcpy_2\arcpy_2.gdb\stops_ms_mitte_buffered",
    buffer_distance_or_field="20 Meters",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR",
    max_deviation="0 DecimalDegrees"
)