# Creating a file dialog to save one file
QFileDialog.getSaveFileName(parent, "Title")

# Creating a file dialog to open one file
res = QFileDialog.getOpenFileName(parent, "Title")
print(res[0])

# Creating a file dialog to open several files
res = QFileDialog.getOpenFileNames(parent, "Title")
print(res[0])