import csv
# csv file path :
# change path !
path="D:\QGISworkspace\PIQUAG"
csv_path = path+'/standard_land_value_muenster.csv'
print(csv_path)

#extend field limit and open csv
csv.field_size_limit(100000000)
file = open(csv_path,'r')
csv_reader=csv.reader(file, delimiter=';',quoting=csv.QUOTE_NONE)

# create temporary layer
layer = QgsVectorLayer("multipolygon", "temp_standard_land_value_muenster", "memory")
layer.setCrs(QgsCoordinateReferenceSystem(25832))

# set fields
provider = layer.dataProvider()
field_1 = QgsField("standard_land_value", QVariant.Double)
field_2 = QgsField("type", QVariant.String)
field_3 = QgsField("district", QVariant.String)
provider.addAttributes([field_1, field_2,field_3])
layer.updateFields()

#skip header
next(csv_reader)
# put rows of csv into a new list
read_features= []
for row in csv_reader:
    read_features.append(row)
#transform rows into features
for row in read_features:
    # get attributes and geometry
    standard_land_value =row[0]
    type =row[1]
    district=row[2]
    geomWKT =row[3]
    geom = QgsGeometry.fromWkt(geomWKT)
    
    # create features and add
    feature_1 = QgsFeature(layer.fields())
    feature_1.setAttribute('standard_land_value', standard_land_value)
    feature_1.setGeometry(geom)
    provider.addFeatures([feature_1])
    
# set paramters for file writer
destCRS = QgsCoordinateReferenceSystem(25832)
fileEncoding = "UTF-8"
driverName ="ESRI Shapefile"
onlySelected = False

# write layer from csv
QgsVectorFileWriter.writeAsVectorFormat(layer, path+"./final_standard_land_value_muenster.shp",
fileEncoding,destCRS, driverName, onlySelected)
# final layer path
final_layer_path =path+"./final_standard_land_value_muenster.shp"
final_layer = QgsVectorLayer(final_layer_path, "Final_Muenster_Dist", "ogr")
# add  final layer to map
QgsProject().instance().addMapLayer(final_layer)