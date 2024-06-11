import csv
def export_feature_csv(layer,outputpath):
    #header for csv
    attributes_header = layer.fields().names()
    # get selected features
    selected_features = layer.selectedFeatures()
    
    features_csv = []
    # get feature data
    for feature in selected_features:
        feature_entry = feature.attributes()
        features_csv.append(feature_entry)
    csv_output= open(outputpath, 'w',newline='')
    writer = csv.writer(csv_output,delimiter=';')
    # write attributes header
    writer.writerow(attributes_header)
    # write features nto csv
    for entry in features_csv:
        writer.writerow(entry)
    


        
    