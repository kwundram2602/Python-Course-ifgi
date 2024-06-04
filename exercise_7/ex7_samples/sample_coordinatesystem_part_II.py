# Create a mapCanvas() instance
mc = iface.mapCanvas()

# Get the layer "Schools.shp"
layer = QgsProject.instance().mapLayersByName("Schools")[0]

# Source coordinate system
crsLayer = layer.crs()

# Target coordinate system
crsTarget = QgsCoordinateReferenceSystem(4326)

# Initializing the transformation
transformation = QgsCoordinateTransform(crsLayer, crsTarget, QgsProject.instance())

# loop through each feature
for feature in layer.getFeatures():
    x = feature.geometry().asPoint().x()
    y = feature.geometry().asPoint().y()
    sourcePoint = QgsPointXY(x, y)
    targetPoint = transformation.transform(sourcePoint)
    print(f"The school has the following UTM coordinates {sourcePoint} and the following WGS84 coordinates {targetPoint}.")