# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PIQAG\PyGIT\PIQGUAG\exercise_8\plugin_folder\mcdt_script\export_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.core import QgsProject
from .create_pdf_profile import *
from .csv_export import export_feature_csv

class Ui_Export_Dialog(object):
    def setupUi(self, Export_Dialog):
        Export_Dialog.setObjectName("Export_Dialog")
        Export_Dialog.resize(400, 186)
        self.ok_quit_box = QtWidgets.QDialogButtonBox(Export_Dialog)
        self.ok_quit_box.setGeometry(QtCore.QRect(50, 150, 341, 32))
        self.ok_quit_box.setOrientation(QtCore.Qt.Horizontal)
        self.ok_quit_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_quit_box.setObjectName("ok_quit_box")
        self.label = QtWidgets.QLabel(Export_Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label.setObjectName("label")
        self.exportPDF_button = QtWidgets.QToolButton(Export_Dialog)
        self.exportPDF_button.setGeometry(QtCore.QRect(20, 50, 171, 19))
        self.exportPDF_button.setObjectName("exportPDF_button")
        self.exportCSV_button = QtWidgets.QToolButton(Export_Dialog)
        self.exportCSV_button.setGeometry(QtCore.QRect(200, 50, 171, 19))
        self.exportCSV_button.setObjectName("exportCSV_button")

        self.retranslateUi(Export_Dialog)
        self.ok_quit_box.accepted.connect(Export_Dialog.accept)
        self.ok_quit_box.rejected.connect(Export_Dialog.reject)
        
        # Connect buttons to the slots
        self.exportPDF_button.clicked.connect(self.select_pdf_file)
        self.exportCSV_button.clicked.connect(self.select_csv_file)
        
        QtCore.QMetaObject.connectSlotsByName(Export_Dialog)

    def retranslateUi(self, Export_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Export_Dialog.setWindowTitle(_translate("Export_Dialog", "Export Dialog"))
        self.label.setText(_translate("Export_Dialog", "Export"))
        self.exportPDF_button.setText(_translate("Export_Dialog", "Export as PDF"))
        self.exportCSV_button.setText(_translate("Export_Dialog", "Export as CSV"))

    def select_pdf_file(self):
        # districts layer
        districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
        selected_features = districts.selectedFeatures()
        if len(selected_features) > 1:
            message_text = f"Es darf nur ein Feature ausgewählt werden für den PDF - Export. Anzahl der ausgewählten Features: {len(selected_features)}"

            # Create MessageBox
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText(message_text)
            msg_box.setWindowTitle("Information")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

            # Anzeigen der QMessageBox
            msg_box.exec_()
            return
        else:
            # pdf file dialog
            fileDialog = QtWidgets.QFileDialog()
            
            fileName, _ = fileDialog.getSaveFileName(None, "Save File", "", "PDF File (*.pdf)")
            # user has chosen file path
            if fileName:
                message_text = f"PDF - Processing...    {fileName}"

                # Create MessageBox
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Information)
                msg_box.setText(message_text)
                msg_box.setWindowTitle("Information")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # Anzeigen der QMessageBox
                msg_box.exec_()
                
                print(f"Selected PDF file: {fileName}")
                # selected feature
                selected_feature = selected_features[0]
                # create image
                pdf_image = districtImage(selected_feature)

                # get name
                dist_name = selected_feature['Name']

                # get geom
                dist_geom = selected_feature.geometry()

                #get area
                dist_area = dist_geom.area()

                #get parent district
                dist_parent = selected_feature["P_District"]
                
                # household, pool and school layer count
                house_number_count = count_of_layer('House_Numbers',dist_geom)
                pool_count = count_of_layer('public_swimming_pools', dist_geom)
                school_count = count_of_layer('Schools',dist_geom)

                # get parcels count
                parcels = QgsProject.instance().mapLayersByName('Muenster_Parcels')[0]
                parcels.removeSelection()
                parcels.selectByExpression("\"Name\" = '{}'".format(dist_name),
                parcels.SetSelection)
                parcels_count = parcels.selectedFeatureCount()

                # inofrmation parsed to pdf 
                dist_infos_dict = {'district_name':dist_name,'parent': dist_parent,
                                    'area':dist_area,'house_number_count':house_number_count,
                                    'parcels_count':parcels_count,'pool_count':pool_count,'school_count':school_count}
                
                # check if pdf was created 
                check_pdf_created=createPDF(fileName,dist_infos_dict,pdf_image)
                if check_pdf_created:
                    message_text = f"PDF - Datei erfolgreich erstellt unter {fileName}"

                    # Create MessageBox
                    msg_box = QtWidgets.QMessageBox()
                    msg_box.setIcon(QtWidgets.QMessageBox.Information)
                    msg_box.setText(message_text)
                    msg_box.setWindowTitle("Information")
                    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    # Anzeigen der QMessageBox
                    msg_box.exec_()
                    return
                else:
                    message_text = f"Error ! - PDF - Datei  nicht erstellt !"

                    # Create MessageBox
                    msg_box = QtWidgets.QMessageBox()
                    msg_box.setIcon(QtWidgets.QMessageBox.Information)
                    msg_box.setText(message_text)
                    msg_box.setWindowTitle("Information")
                    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    # Anzeigen der QMessageBox
                    msg_box.exec_()
                    return
            # check pdf file dialog result
            result = fileDialog.result()
            # user has canceled file dialog
            if result == 0:
                print("PDF - Creation was canceled")
                message_text = "PDF - Creation was canceled"

                # Create MessageBox
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Information)
                msg_box.setText(message_text)
                msg_box.setWindowTitle("Information")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # Anzeigen der QMessageBox
                msg_box.exec_()
                return
                    
    # user clicked CSV export
    def select_csv_file(self):
        # file dialog
        fileDialog = QtWidgets.QFileDialog()
        fileName, _ = fileDialog.getSaveFileName(None, "Save File", "", "CSV File (*.csv)")
        # when file path was chosen
        if fileName:
            print(f"Selected CSV file: {fileName}")
            # districts layer
            districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
            # export selected fratures as csv
            check_if_csv_created=export_feature_csv(districts,fileName)
            if check_if_csv_created:
                message_text = f"CSV - Datei erfolgreich erstellt unter {fileName}"

                # Create MessageBox
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Information)
                msg_box.setText(message_text)
                msg_box.setWindowTitle("Information")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # Anzeigen der QMessageBox
                msg_box.exec_()
                return
            # no csv file created
            else:
                message_text = f"Error ! - CSV - Datei  nicht erstellt !"

                # Create MessageBox
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Information)
                msg_box.setText(message_text)
                msg_box.setWindowTitle("Information")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # Anzeigen der QMessageBox
                msg_box.exec_()
                return
        # check result of file dialog
        result = fileDialog.result()
        # user canceled file dialog
        if result == 0:
            print("CSV - Creation was canceled")
            message_text = "CSV - Creation was canceled"

            # Create MessageBox
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText(message_text)
            msg_box.setWindowTitle("Information")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

            # Anzeigen der QMessageBox
            msg_box.exec_()
            return
              
