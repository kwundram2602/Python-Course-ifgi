# Creating a parent object
parent = iface.mainWindow()

# Creating a QMessageBox with level 'Warning'
res = QMessageBox.information(parent, "Python in QGIS & ArcGIS", "Welcome to the course!", QMessageBox.Yes | QMessageBox.No)
if res == QMessageBox.Yes:
    print("User clicked on 'Ok'")
else:
    print("User canceled the action.")