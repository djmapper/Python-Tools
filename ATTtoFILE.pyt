import os, arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python ToolBox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]

class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Attachments to File"
        self.description = "Extract attachments from a feature class to file"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
        displayName="Attachment Table Name",
        name="att_table",
        datatype="DETable",
        parameterType="Required",
        direction="Input")
	
	param1 = arcpy.Parameter(
        displayName="Data Field",
        name="fldBLOB",
        datatype="Field",
        parameterType="Required",
        direction="Input")
	
	param1.parameterDependencies = [param0.name]
	
	param2 = arcpy.Parameter(
        displayName="Attachment Name Field",
        name="fldAttName",
        datatype="Field",
        parameterType="Required",
        direction="Input")
	
	param2.parameterDependencies = [param0.name]	

        param3 = arcpy.Parameter(
        displayName="Attachment output Folder",
        name="outFolder",
        datatype="DEFolder",
        parameterType="Required",
        direction="Input")
        
        params = [param0, param1, param2, param3]
        
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
    	tbl =  parameters[0].valueAsText
        fldBLOB =  parameters[1].valueAsText
        fldAttName =  parameters[2].valueAsText
        outFolder =  parameters[3].valueAsText
        with arcpy.da.SearchCursor(tbl,[fldBLOB, fldAttName]) as cursor:
            for row in cursor:
                binaryRep = row[0]
                fileName = row [1]
                #save to disk
                open(outFolder + os.sep +fileName, 'wb').write(binaryRep.tobytes())
        return