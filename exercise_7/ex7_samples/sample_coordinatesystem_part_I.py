# Get the layer "Muenster_City_Districts.shp"
layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]

# Get CRS object
crs = layer.crs()
print(crs)

# Check if crs is Valid
print(crs.isValid())

# Get the description of the crs
print(crs.description())

# Get the Proj4 of the crs
print(crs.toProj4())

# Get the WKT of the crs
print(crs.toWkt())
