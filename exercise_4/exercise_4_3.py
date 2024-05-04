# Import modules
from qgis.core import QgsVectorLayer, QgsProject,QgsApplication
from qgis.core import *
import os , sys


# Supply path to qgis install location
#QgsApplication.setPrefixPath("/path/to/qgis/installation", True)
QgsApplication.setPrefixPath(r"D:\QGISversions\QGIS_3.34.5", True)
# Path to data and QGIS-project
#layer_path = r"C:\Users\Sven Harpering\sciebo\GIS-GK\GIS-GK_WS_23_24\GIS Data\Flughafen Muenchen - Datenlieferung I\WKA_Buffer.shp"
layer_path = r"D:\QGISworkspace\PIQUAG\Muenster\\"
project_path = r"D:\QGISworkspace\PIQUAG\Test"  # for QGIS version 3+

dir_list = os.listdir(layer_path)
final_list = []
#print(dir_list)
for f in dir_list:
    name, ext = os.path.splitext(f)
    if ext == '.shp':
        final_list.append(f)
print("Shapefiles:\n",final_list)

i=0
for file in final_list:
    
    file = layer_path+file
    final_list[i]=file
    i+=1
    
# Create layer
print("final_list:\n",final_list)
for shps in final_list:
    print ("file path:\n "+ shps)
    
    basename = os.path.basename(shps)
    name, ext = os.path.splitext(basename)
    shp = QgsVectorLayer(shps, name, "ogr")
    # Check if layer is valid
    if not shp.isValid():
        print("Error loading the layer!")
    else:
    # Create QGIS instance and "open" the project
        try:
            project = QgsProject.instance()
        except Exception:
            print("error returning project instance")    
        project.read(project_path)

    # Add layer to project
        project.addMapLayer(shp)

    # Save project
        project.write(project_path+r"\myFirstProject.qgz")
        

        print(f"{name} added to project\nProject saved successfully!")