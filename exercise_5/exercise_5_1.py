import processing
mc = iface.mapCanvas()
parent = iface.mainWindow()
districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')
districts = districts[0]
schools = QgsProject.instance().mapLayersByName('Schools')[0]

print(districts)
district_names =[]
# Ordering
request = QgsFeatureRequest()
nameClause = QgsFeatureRequest.OrderByClause("Name",
ascending = True)
orderby = QgsFeatureRequest.OrderBy([nameClause])
request.setOrderBy(orderby)

for feature in districts.getFeatures(request):
    name= feature['NAME']
    district_names.append(name)
    
#district_names =district_names.sort()
sDistrict, bOk = QInputDialog.getItem(parent,
"District Names", "Select District: ",
district_names)

if(bOk==False):
    QMessageBox.warning(parent, "Schools", "User cancelled")
else:
    
    print('sDistrict:', sDistrict)
    districts.selectByExpression("\"Name\" = '{}'".format(sDistrict),
    districts.SetSelection)
    mc.zoomToSelected()
    selected= districts.selectedFeatures()[0]
    #print(selected.attributes())
    dist_geom = selected.geometry()
    
    schools.removeSelection()
    # school ordering request
    request = QgsFeatureRequest()
    nameClause = QgsFeatureRequest.OrderByClause("NAME",
    ascending = False)
    orderby = QgsFeatureRequest.OrderBy([nameClause])
    request.setOrderBy(orderby)
    for school in schools.getFeatures(request):
        x = school.geometry().get().x()
        y = school.geometry().get().y()
        if(school.geometry().within(dist_geom)):
            schools.selectByIds([school.id()],QgsVectorLayer.AddToSelection)
        
        
    if(schools.selectedFeatureCount()>0):
        #selected Schools
        selected_schools= schools.selectedFeatures()
        #print("selected schools:", selected_schools)
    else:
        # no schools in district
        print("no schools in this district")
        selected_schools=None
        QMessageBox.warning(parent,"Warning", f"There are no schools in the district {sDistrict}")
    if(selected_schools!=None):
        
        schoolDict ={}
        for feature in selected_schools:
            name= feature['NAME']
            type = feature['SchoolType']
            geom = feature.geometry()
            distance= geom.distance(dist_geom)
            schoolDict[name] = type
        print(schoolDict)
            
        # show information 
        QMessageBox.warning(parent,
        f"Schools in {sDistrict}",
        f"The selcted District is {selected['Name']}.\n Amount of {schools.selectedFeatureCount()} school/s in this district: \n{sorted(schoolDict.items())} ")
