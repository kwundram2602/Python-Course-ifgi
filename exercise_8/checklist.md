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

pyuic5 "D:\PIQAG\PyGIT\PIQGUAG\exercise_8\plugin_folder\mcdt_script\single_district_dialog.ui" -o "D:\PIQAG\PyGIT\PIQGUAG\exercise_8\plugin_folder\mcdt_script\single_district_dialog.py"


 # after creating plugin folder
 
In your plugin directory, compile the resources file using pyrcc5 (simply run make if you have automake or use pb_tool) 
Test the generated sources using make test (or run tests from your IDE) 
Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below) 
Test the plugin by enabling it in the QGIS plugin manager 
Customize it by editing the implementation file exercise_8_1.py 
Create your own custom icon, replacing the default icon.png 
Modify your user interface by opening exercise_8_1_dockwidget_base.ui in Qt Designer 

Notes: 
You can use the Makefile to compile and deploy when you make changes. This requires GNU make (gmake). The Makefile is ready to use, however you will have to edit it to add addional Python source files, dialogs, and translations. 
You can also use pb_tool to compile and deploy your plugin. Tweak the pb_tool.cfg file included with your plugin as you add files. Install pb_tool using pip or easy_install. See http://loc8.cc/pb_tool for more information. 
For information on writing PyQGIS code, see http://loc8.cc/pyqgis_resources for a list of resources. 


The Plugin Builder creates several Python files that are relevant for you:
▪ __init__.py
▪ Initializes the code and serves as package manager (not really necessary anymore since Python 3.3)

▪ yourScript.py
▪ Contains logic to add and remove the plugin from the QGIS interface, to translate the plugin, initialize
the GUI and to run your algorithm

▪ yourScript_dialog.py
▪ Contains logic for your dialog (e.g. event handling when a user clicks a button in that GUI,…)
---------------------------------------------------------------
▪ Write your code in yourScript.py and call the GUIs
from the other Python files here
or
▪ Write your code directly in the Python files that
create the GUIs
or
▪ Write your functionality in new Python files and
import them so that they can be used

## Guis
When creating additional GUIs, you have to transform the *.ui files to *.py files. This is
only done for the first GUI automatically during the process of configuring the plugin
with the Plugin Builder.
▪ Start C:\Program Files\QGIS 3.34.4\OSGeo4W.bat
▪ Use this prompt for each *.ui file you want to transform to a *.py file
pyuic5 “xy.ui“ -o “xy.py“
▪ Use the full path to the files!
▪ If you re-use this prompt, all changes in the *.py file are gone!

https://doc.qt.io/qt-5/qtwidgets-module.html


While scripting you can reload your plugin so that you can see the changes
directly without restarting QGIS
▪ Go to Plugin > Plugin Reloader > Choose a plugin to be reloaded
▪ Recommendation: Test your plugin after each bigger step!
▪ Share the Plugin at the end
▪ Go to the project folder of the plugin, zip the whole folder and share it with others
▪ Other users has to unzip the file in their plugin-directory
▪ Upload it to the QGIS Plugin Repository
