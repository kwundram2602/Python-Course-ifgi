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
# install reportlab
import pip
pip.main(['install', 'reportlab'])

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

class CreateCityDistrictProfile(QgsProcessingAlgorithm):
    """
    This processing script creates a PDF profile for a specific city district.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    DISTRICTNAME = 'DISTRICTNAME'
    POINTINPUT = 'POINTINPUT'
    OUTPUT = 'OUTPUT'
    

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
        return self.tr('Layer tools')

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

    
      
    def createPDF(self,parameters):
        
        return 0  
    
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
            print(district_names)
            return district_names
        
        
        # create list of district names. Use user defined function
        param_name_list= alphabeticalDistrictList()
        
        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.DISTRICTNAME,
                self.tr('District Name'),
                param_name_list
            )
        )
        
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.POINTINPUT,
                self.tr('Input point layer'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        #pdf_output = self.parameterAsFileOutput(parameters,'PDF_OUTPUT',context)
        #self.createPDF(pdf_output)
       
        
        return {self.OUTPUT: "Template"}
