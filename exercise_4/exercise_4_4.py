# change folder paths
districts = r'D:/QGISworkspace/PIQUAG/Muenster/Muenster_City_Districts.shp'
points = r'D:/QGISworkspace/PIQUAG/Muenster/Schools.shp'
# change name if file already exists or delete file
output = r'D:/QGISworkspace/PIQUAG/countedSchools7.gpkg'
processing.run("native:countpointsinpolygon",
{'POLYGONS':districts,
'POINTS':points,
'WEIGHT':'','CLASSFIELD':'',
'FIELD':'CountedSchools','OUTPUT':output})
vlayer = QgsVectorLayer(output, "CountedSchools", "ogr")
mc = iface.mapCanvas()
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    

features =vlayer.getFeatures()
print(vlayer.fields())
for feature in features:
    
    print(feature['P_District'], feature['CountedSchools'])