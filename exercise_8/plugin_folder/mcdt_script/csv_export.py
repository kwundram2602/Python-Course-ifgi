import csv 
from .create_pdf_profile import count_of_layer
from qgis.core import QgsProject
# ouputpath mus be raw string containing filename and .csv
def export_feature_csv(layer,outputpath):
    print(outputpath)
     
    #header for csv
    attributes_header = layer.fields().names()
    attributes_header.append("size_Parcels")
    attributes_header.append("number_Parcels")
    attributes_header.append("number_schools")
    # get selected features
    selected_features = layer.selectedFeatures()
    
    features_csv = []
    parcels = QgsProject.instance().mapLayersByName('Muenster_Parcels')[0]

    # get feature data
    for feature in selected_features:
        # name of district
        district_name_title = feature["Name"]
        # parcels
        parcels.removeSelection()
        parcels.selectByExpression("\"Name\" = '{}'".format(district_name_title),
        parcels.SetSelection)
        # parcels count
        parcels_count=parcels.selectedFeatureCount()
        # size init
        size_Parcels= 0
        for parcel in parcels.selectedFeatures():
            size_Parcels = size_Parcels + parcel.geometry().area()
        
        feature_geom = feature.geometry()
        feature_entry = feature.attributes()
        # number of schools
        number_schools = count_of_layer("Schools",feature_geom)
        # add attributes
        feature_entry.append(size_Parcels)
        feature_entry.append(parcels_count)
        feature_entry.append(number_schools)
        features_csv.append(feature_entry)
    # open csv
    with open(outputpath, 'w',newline='') as csv_output:
        writer = csv.writer(csv_output,delimiter=';')
        # write attributes header
        writer.writerow(attributes_header)
        # write features into csv
        for entry in features_csv:
            writer.writerow(entry)
    # close csv
    csv_output.close()
    return True