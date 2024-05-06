mc = iface.mapCanvas()
import csv

path=QgsProject.instance().readPath("./")
#print("PATH: ", path)
schoolreport= open(path+'/SchoolReport.csv', 'w',newline='') 
writer = csv.writer(schoolreport,delimiter=';')
writer.writerow(['Name','X','Y'])

schools= mc.currentLayer()

#schoolFeatures =schools.getFeatures()
selectedSchools= schools.selectedFeatures()
#print(selectedSchools)

for feature in selectedSchools:
    xyGeom = feature.geometry()
    pt = xyGeom.asPoint()
    xcoord = pt.x()
    ycoord = pt.y()
    name = feature.attributes()
    output = [name[1],xcoord,ycoord]
    print(output[2])
    writer.writerow(output)