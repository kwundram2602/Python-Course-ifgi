import processing
mc = iface.mapCanvas()
districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')
districts = districts[0]

points = QgsProject.instance().mapLayersByName('Schools')
points=points[0]

pointsTool = processing.run("qgis:countpointsinpolygon",
{'POLYGONS':districts,
'POINTS':points,
'WEIGHT':'','CLASSFIELD':'',
'FIELD':None,'OUTPUT':'TEMPORARY_OUTPUT'})

countLayer = pointsTool['OUTPUT']
dict = {}


for feature in countLayer.getFeatures():
    district= feature['P_DISTRICT']
    numberSchools = feature['NUMPOINTS']
    
    if district in dict:
        dict[district] += numberSchools
    else:
        dict[district] = numberSchools

for district, schools in dict.items():
    print(district , schools)
        