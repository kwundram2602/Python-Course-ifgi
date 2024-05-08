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
    #create Request for getting district
#    request_dist = QgsFeatureRequest()
#    request_dist.setFilterExpression(
#    f"\"Name\" == {sDistrict}")
    print('sDistrict:', sDistrict)
    districts.selectByExpression("\"Name\" = '{}'".format(sDistrict),
    districts.SetSelection)
    mc.zoomToSelected()
    selected= districts.selectedFeatures()[0]
    print(selected.attributes())
    
    QMessageBox.warning(parent,
    f"Schools in {sDistrict}",
    f"The selcted District is {selected['Name']}.\n Hallo")
