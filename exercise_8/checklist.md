# Checklist

 1. Install and configure an IDE

 2. Create a „compile.bat“ file to „create“ the plugin

 3. Install the plugin „Plugin Builder“ in QGIS

 4. Install the plugin „Plugin Reloader“ in QGIS

 5. Use the „Plugin Builder“ to create the structure of your new plugin

 6. Use the „compile.bat“ file to compile „resources.qrc“

 7. Copy the plugin-folder to your profile folder

 8. Change the GUI by using Qt Designer

 9. Add some specific processing code that fit your needs

 10. Reload, test and share the plugin



 # after creating plugin folder
 
In your plugin directory, compile the resources file using pyrcc5 (simply run make if you have automake or use pb_tool) 
Test the generated sources using make test (or run tests from your IDE) 
Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below) 
Test the plugin by enabling it in the QGIS plugin manager 
Customize it by editing the implementation file exercise_8_1.py 
Create your own custom icon, replacing the default icon.png 
Modify your user interface by opening exercise_8_1_dockwidget_base.ui in Qt Designer 

