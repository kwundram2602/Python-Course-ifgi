import arcpy

class ToolValidator:
    def __init__(self): 
        self.params = arcpy.GetParameterInfo()
        try:
            arcpy.Delete_management('in_memory\\freq_table')
        except:
            pass

    def initializeParameters(self):
        return

    def updateParameters(self):
        # if feature class is set,provide Values for Parameter 1: name_field       
        if self.params[0].altered:
            # Use the Describe Function to get Details (field names) for Input FC
            fields = arcpy.Describe(self.params[0]).fields
            field_names = [x.name for x in fields]
            # set the field names as filter for parameter [1]
            self.params[1].filter.list = field_names

        # if name field is selected provide values (all unique field values) for parameter 2: name_value
        if self.params[1].altered and self.params[0].altered:
            # get a table of the unique values for the name field
            arcpy.analysis.Frequency(in_table=self.params[0].value,out_table='in_memory\\freq_table',frequency_fields=self.params[1].value)
            name_values = [row[0] for row in arcpy.da.SearchCursor(in_table='in_memory\\freq_table', field_names=[self.params[1].value])]
            #delete the table in memory
            arcpy.Delete_management('in_memory\\freq_table')
            #set the parameter filter list
            self.params[2].filter.list = name_values

        
        return

    def updateMessages(self):
        return