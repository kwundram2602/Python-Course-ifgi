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

#import os
import os

#import qgis modules
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,QgsProject,
                        QgsVectorLayer,
                        QgsCoordinateTransform,
                        QgsPointXY,
                        QgsRectangle,
                       QgsProcessingParameterFileDestination,
                       QgsFeatureSink,
                       QgsCoordinateReferenceSystem,
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
    def createPDF(self, outputPath, attributeDict, picturePath):
        # create canvas
        c = canvas.Canvas(outputPath,pagesize = letter)
        
        # set font
        c.setFont("Helvetica", 20)
        
        #write title
        c.drawString(150,760,f"Information for the district '{attributeDict['district_name']}'")
        
        #set font
        c.setFont("Helvetica", 14)
        
        #write information
        c.drawString(100,735,f"The parent district is : {attributeDict['parent']}.")
        c.drawString(100,705,f"The district has an area of {attributeDict['area']} m^2.")
        c.drawString(100,690,f"The district has  {attributeDict['house_number_count']} housenumbers.")
        c.drawString(100,675,f"The district contains {attributeDict['parcels_count']} parcels.")
        
        #if schools or pools are selected
        if (attributeDict['counted_property']!="None"):
            c.drawString(100,650,f"The counted property is '{attributeDict['counted_property']}'. There are {attributeDict['pool_or_school_count']} objects of this property.")
        
        #when not selected
        else:
            c.drawString(100,650,f"Please select pools or schools as point input.")
        
        # draw image of map when picturePath is given
        if picturePath:
            c.drawString(100,600,"Map of selected disrict:")
            c.drawImage(picturePath,100, 270, width = 400 , height = 300)
        
        #save canvas
        c.save()
        
    def districtImage(self, selected_district):
        # get districts
        districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]

        # get district geometry
        selected_district_geometry=selected_district.geometry()
        # layer crs for transformation
        crsLayer = districts.crs()
        # Target coordinate system
        crsTarget = QgsCoordinateReferenceSystem(3857)
        # Initializing the transformation
        transformation = QgsCoordinateTransform(crsLayer, crsTarget, QgsProject.instance())
        
        #get district boundingBox
        district_boundingBox = selected_district_geometry.boundingBox()
        
        xMax = district_boundingBox.xMaximum()
        xMin = district_boundingBox.xMinimum()
        yMax = district_boundingBox.yMaximum() 
        yMin = district_boundingBox.yMinimum()
        # use points of bbox
        pointLeftBottom=QgsPointXY(xMin,yMin)
        pointRightTop= QgsPointXY(xMax,yMax)
        
        #transform points
        pointLeftBottom=transformation.transform(pointLeftBottom)
        pointRightTop=transformation.transform(pointRightTop)
        
        # use transoformed points
        bbox_transformed= QgsRectangle(pointLeftBottom,pointRightTop)
        
        #set extent
        iface.mapCanvas().setExtent(bbox_transformed)
        
        #refresh map
        iface.mapCanvas().refresh()
        
        #wait 5 sec
        time.sleep(5)
        
        #create file path and returning it
        picturePath = os.path.join(QgsProject.instance().homePath(), "map.png")        
        
        #save Image
        iface.mapCanvas().saveAsImage(picturePath)
        
        #return image path
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
    
    # function definition to get alphabetical list
    def alphabeticalDistrictList(self):
        # district layer
        districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
        
        # request order by nameclause
        request = QgsFeatureRequest()
        nameClause = QgsFeatureRequest.OrderByClause("Name",ascending = True)
        orderby = QgsFeatureRequest.OrderBy([nameClause])
        request.setOrderBy(orderby)

        # name list 
        district_names =[]
        for feature in districts.getFeatures(request):
            name= feature['NAME']
            district_names.append(name)
        return district_names
    
    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        
        # create list of district names. Use user defined function
        param_name_list= self.alphabeticalDistrictList()
        
        # district name parameter
        self.addParameter(
            QgsProcessingParameterEnum(
                self.DISTRICTNAME,
                self.tr('District Name'),
                param_name_list
            )
        )
        # point input paramter : pools or schools. other point layers can still be selected but are not used
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.POINTINPUT,
                self.tr('Input point layer. Select Pools or Schools'),
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
    # computes count of point layer in district(dist_geom)
    def count_of_layer(self,layer_name,dist_geom):
        # loads layer by layer_name
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        
        # clears selection first
        layer.removeSelection()
        
        # get count of layer in district
        for feature in layer.getFeatures():
            if(feature.geometry().within(dist_geom)):
                layer.selectByIds([feature.id()],QgsVectorLayer.AddToSelection)
                
        # when there are features in the district   
        if(layer.selectedFeatureCount()>0):
        #selected features count
            feature_count=layer.selectedFeatureCount()
            
        # no features in district
        else:
            print(f"no features of {layer_name} in this district")
            feature_count=0
                        
        return feature_count

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        # create list of district names. Use user defined function
        param_name_list= self.alphabeticalDistrictList()
        
        # load districts layer
        districts = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
        
        #get name of chosen district
        district_name_index = self.parameterAsInt(parameters,'DISTRICTNAME',context)
        district_name_title= param_name_list[district_name_index]
        
        # get parent district
        districts.selectByExpression("\"Name\" = '{}'".format(district_name_title),
        districts.SetSelection)
        selected_dist= districts.selectedFeatures()[0]
        parent =selected_dist["P_District"]
        
        # get geom
        dist_geom =selected_dist.geometry()
        
        #get area
        dist_area = dist_geom.area()
        
        # household layer count
        house_number_count = self.count_of_layer('House_Numbers',dist_geom)
        
        # parcels count
        parcels = QgsProject.instance().mapLayersByName('Muenster_Parcels')[0]
        parcels.removeSelection()
        parcels.selectByExpression("\"Name\" = '{}'".format(district_name_title),
        parcels.SetSelection)
        parcels_count=parcels.selectedFeatureCount()
        
        # pools or schools count
        point_input = self.parameterAsCompatibleSourceLayerPath(parameters,
        'POINTINPUT',context,compatibleFormats =['shp'])
        # pools selected
        if (point_input.endswith("public_swimming_pools.shp")):
            pool_or_school_count= self.count_of_layer('public_swimming_pools',dist_geom)
            counted_property="Pools"
        # schools selected
        elif(point_input.endswith("Schools.shp")):
            pool_or_school_count= self.count_of_layer('Schools',dist_geom)
            counted_property="Schools"
        # none of them selected
        else:
            pool_or_school_count= 0
            counted_property="None"
            
        #pdf output
        pdf_output = self.parameterAsFileOutput(parameters,'PDF_OUTPUT',context)
        print(f"Creating PDF for district: {parameters} at {pdf_output}")
        
        # information for pdf create
        dist_infos_dict = {'district_name':district_name_title,'parent': parent,
        'area':dist_area,'house_number_count':house_number_count,'parcels_count':parcels_count,
        'counted_property':counted_property,'pool_or_school_count':pool_or_school_count}
        
        #Create picturePath 
        picturePath = self.districtImage(selected_dist)
        
        #create pdf
        self.createPDF(pdf_output,dist_infos_dict, picturePath)
        
        # return for debug
        return {'PDF_OUTPUT': pdf_output, 'Point':point_input,'district_name':district_name_title,'parent': parent,
        'area':dist_area,'house_number_count':house_number_count,'parcels_count':parcels_count,
        'counted_property':counted_property,'pool_or_school_count':pool_or_school_count}
