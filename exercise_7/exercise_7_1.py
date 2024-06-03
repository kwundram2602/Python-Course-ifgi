"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
# imports

#install reportlab
#import pip
#pip.main(['install', 'reportlab'])

#import reportlap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#import time
import time

#import qgis modules
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,QgsProject,
                       QgsProcessingParameterFileDestination,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsFeatureRequest,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterString,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterFeatureSource,
                       
                       QgsProcessingParameterFeatureSink)
from qgis import processing
from qgis.utils import iface




class CreateCityDistrictProfile(QgsProcessingAlgorithm):
    """
    This processing script creates a PDF profile for a specific city district.
    """
    

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    DISTRICTNAME = 'DISTRICTNAME'
    POINTINPUT = 'POINTINPUT'
    PDFOUTPUT = 'PDF_OUTPUT'
    
    # create pdf function
    def createPDF(self, outputPath, attributeListe):
        c = canvas.Canvas(outputPath,pagesize = letter)
        c.setFont("Helvetica", 12)
        c.drawString(100,750,"Test")
        
        #if picturePath:
           # c.drawImage(picturePath,50, 50, width = 100 , height = 100)
        c.save()
        
    def districtImage(self, selected_district):
        district_geometry = selected_district.geometry()
        district_boundingBox = district_geometry.boundingBox()
        iface.mapCanvas().setExtent(district_boundingBox)
        iface.mapCanvas().refresh()
        time.sleep(5)
        
        # Create a temporary file path and returning it
        temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        picturePath = temp_file.name
        temp_file.close()

        iface.mapCanvas().saveAsImage(picturePath)
        return picturePath
    
    
    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateCityDistrictProfile()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. 
        """
        return 'createcitydistrictprofile'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Create City District Profile')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Layer tools. ')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'layertools'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This processing script creates a PDF profile for a specific city district.")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        
        
        # function definition to get alphabetical list
        def alphabeticalDistrictList():
        # district layer
            districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
            # request order by nameclause
            request = QgsFeatureRequest()
            nameClause = QgsFeatureRequest.OrderByClause("Name",
            ascending = True)
            orderby = QgsFeatureRequest.OrderBy([nameClause])
            request.setOrderBy(orderby)

            # name list 
            district_names =[]
            for feature in districts.getFeatures(request):
                name= feature['NAME']
                district_names.append(name)
            
            return district_names
        
        
        # create list of district names. Use user defined function
        param_name_list= alphabeticalDistrictList()
        
        # district name parameter
        self.addParameter(
            QgsProcessingParameterEnum(
                self.DISTRICTNAME,
                self.tr('District Name'),
                param_name_list
            )
        )
        # point input paramter : pools or schools
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.POINTINPUT,
                self.tr('Input point layer'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

        # pdf output. user can set destination
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.PDFOUTPUT,
                self.tr('PDF Output '),
                fileFilter='PDF files (*.pdf)'
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        
        #Create picturePath 
        #picturePath = self.districtImage()
         
        pdf_output = self.parameterAsFileOutput(parameters,'PDF_OUTPUT',context)
        print(f"Creating PDF for district: {parameters} at {pdf_output}")
        
        
        self.createPDF(pdf_output,"testlayer")
        
       
        
        return {'PDF_OUTPUT': pdf_output}
