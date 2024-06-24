import arcpy
arcpy.analysis.Near("point_for_test",
                    "stops_ms_mitte", None,
                    "LOCATION", "NO_ANGLE",
                    "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST;NEAR_X NEAR_X;NEAR_Y NEAR_Y")
