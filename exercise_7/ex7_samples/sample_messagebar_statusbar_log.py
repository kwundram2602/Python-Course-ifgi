# Showing a message in the message bar
iface.messageBar().pushMessage("Welcome to Python in QGIS & ArcGIS", "I am happy that you attend the course.", level = Qgis.Success, duration = 5)

# Showing a message in the status bar
iface.mainWindow().statusBar().showMessage("Welcome to Python in QGIS & ArcGIS")

# Writing a message to the logging
QgsMessageLog.logMessage("Message", "Python Course", level = Qgis.Info)
