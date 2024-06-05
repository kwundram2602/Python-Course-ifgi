# Creating a parent object
parent = iface.mainWindow()

# Creating a QInputDialog to get a text input
# Function returns two values, the input and a status
sValue, bOk = QInputDialog.getText(parent, "Get Layer", "Please enter layer name", text=mc.currentLayer().sourceName())

# if the status is True (means user clicked an "ok" print something)
if bOk:
    print(f"User entered: {sValue}")
# status False (used clicked "candel")
else:
    print("User canceled")

# Creating a QInputDialog to get a inteeger input
iValue, bOk = QInputDialog.getInt(parent, "Get Integer", "Please enter a number", 5, 0, 10, 2)
if bOk:
    print(f"User entered: {iValue}")
else:
    print("User canceled")

# Creating a QInputDialog to get a double input
dValue, bOk = QInputDialog.getDouble(parent, "Get Double", "Please enter a number", 7.5, 0, 10, 2)
if bOk:
    print(f"User entered: {dValue}")
else:
    print("User canceled")
    
# Creating a QInputDialog to get a value from a list
itemList = ["Value A", "Value B", "Value C"]
lValue, bOk = QInputDialog.getItem(parent, "Get Item", "Please choose an itme", itemList, editable = False)
if bOk:
    print(f"User entered: {lValue}")
else:
    print("User canceled")

