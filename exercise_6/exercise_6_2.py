# Creating map canvas
mc = iface.mapCanvas()

# Get public_swimming_pools layer
layer = QgsProject.instance().mapLayersByName("public_swimming_pools")[0]

# Get city districts
city_districts = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]


# Getting fields of layer
fields = layer.fields()

# Getting the layers data provider
provider = layer.dataProvider()

# Getting capabilities of layer
capabilities = provider.capabilitiesString()

# Check if atrributes can be changed (had to check in german, if its not working change to english)
if "Attributwerte ändern" in capabilities:

    # Iterate through all features of layer
    for feature in layer.getFeatures():
        # Get id of current feature
        feature_id = feature.id()
        # If type is H change atrribute to Hallenbad
        if feature["Type"] == "H":
            attributes = {fields.indexOf("Type"):"Hallenbad"}
            provider.changeAttributeValues({feature_id:attributes})
        
        # If type is F change atrribute to Freibad
        elif feature["Type"] == "F":
            attributes = {fields.indexOf("Type"):"Freibad"}
            provider.changeAttributeValues({feature_id:attributes})
else:
    print("Attributes cannot be changed")

# Add field_added variable
field_added = False

# Check if atrributes can be added (had to check in german, if its not working change to english)
if "Attribute hinzufügen" in capabilities:
    
    # Create new district field
    district_field = QgsField("district", QVariant.String, len = 50)

    # Use the data provider to add the fields to layer
    provider.addAttributes([district_field])
    
    # Use the method updateFields() to show them in layer
    layer.updateFields()
    
    # Set the field_added variable to true
    field_added = True
    
else: 
    print("Fields cannot be added to the layer")
    
# Check if atrributes can be changed (had to check in german, if its not working change to english)
# Check if field was added
if "Attributwerte ändern" in capabilities and field_added:
    
    # Iterate through features of layer
    for feature in layer.getFeatures():
        
        # Iterate through features of districts
        for district in city_districts.getFeatures():
            
            # Getting geometry of feature 
            feature_geometry  = feature.geometry()
            
            # Getting geometry of district 
            district_geometry = district.geometry()
            
            # Check if feature is within district
            if feature_geometry.within(district_geometry):
                
                # Assign district name
                district_name = district["Name"]
                
                # Getting feature id
                feature_id = feature.id()
                
                #Load in the new layer fields
                fieldsnew = layer.fields() 
                                
                # assign attributes
                attributes = {fieldsnew.indexOf("district"): district_name}
                
                # Use the data provider to add the fields to layer
                provider.changeAttributeValues({feature_id:attributes})
                
                # Use the method updateFields() to show them in layer
                layer.updateFields()

else:
    print("Attributes cannot be changed")

