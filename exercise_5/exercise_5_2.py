# Create input window
parent = iface.mainWindow()
sCoords, bOK = QInputDialog.getText(parent, "Coordinates", "Enter coordinates as latitude, longitude", text = "51.96066,7.62476")

# read in coordinates
sCoordsSplit = sCoords.split(",")
lat = float(sCoordsSplit[0])
lon = float(sCoordsSplit[1])

# transform coordinates
layer = layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]
coordFrom = QgsCoordinateReferenceSystem(4326)
coordTo = layer.crs()

transformation = QgsCoordinateTransform(coordFrom, coordTo, QgsProject.instance())
pointFrom = QgsPointXY(lon,lat)
pointTo = transformation.transform(pointFrom)

# Check if point is in district and display popup
executed = False
for feature in layer.getFeatures():
    if feature.geometry().contains(QgsGeometry.fromPointXY(pointTo)):
        print("yes")
        QMessageBox.information(None, "", "Der Punkt liegt im folgendem Gebiet: {}".format(feature["Name"]))
        executed = True

# display popup if point is not within district
if not executed:
    QMessageBox.information(None, "", "Der Punkt liegt in keinem Gebiet")


