class ToolValidator:
    # Class to add custom behavior and properties to the tool and tool parameters.

    def __init__(self):
        # set self.params for use in other function
        self.params = arcpy.GetParameterInfo()
        try:
            arcpy.Delete_management('in_memory\\freq_table')
        except:
            pass

    def initializeParameters(self):
        # Customize parameter properties. 
        # This gets called when the tool is opened.
        return

    def updateParameters(self):
        # Modify parameter values and properties.
        # This gets called each time a parameter is modified, before 
        # standard validation.
        if self.params[1].altered:
            # Use the Describe Function to get Details (field names) for Input FC
            fields = arcpy.Describe(self.params[1]).fields
            field_names = [x.name for x in fields]
            # set the field names as filter for parameter [1]
            self.params[2].filter.list = field_names
            
        # if name field is selected provide values (all unique field values) for parameter 2: name_value
        if self.params[2].altered and self.params[1].altered:
            # get a table of the unique values for the name field
            arcpy.analysis.Frequency(in_table=self.params[1].value,out_table='in_memory\\freq_table',frequency_fields=self.params[2].value)
            name_values = [row[0] for row in arcpy.da.SearchCursor(in_table='in_memory\\freq_table', field_names=[self.params[2].value])]
            #delete the table in memory
            arcpy.Delete_management('in_memory\\freq_table')
            #set the parameter filter list
            self.params[3].filter.list = name_values
        return

    def updateMessages(self):
        # Customize messages for the parameters.
        # This gets called after standard validation.
        return

    # def isLicensed(self):
    #     # set tool isLicensed.
    #     return True