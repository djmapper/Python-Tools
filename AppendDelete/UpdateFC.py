import arcpy
# set workspace
arcpy.env.workspace = r"C://_Temp//data.gdb"
# set source data connection
cliveDC = r"Database Connections\\DBSERVER@Geodata_gis.sde\\KCDC\\"
# list of feature classes in workspace
fcs = arcpy.ListFeatureClasses()

# define processes 
def process_NZAA():
    print "Empty process"
def process_NZAA_1():
    print "process NZAA_1 data"
    arcpy.DeleteFeatures_management(fc)
    arcpy.Append_management(cliveDC + "NZAA", fc, "NO_TEST")
def process_NZAA_2():
    print "process NZAA_2 data"
    arcpy.DeleteFeatures_management(fc)
    arcpy.Append_management(cliveDC + "NZAA", fc, "NO_TEST")

# process each feature class in list
for fc in fcs: 
    # data dictionary for feature class : process
    options = {'NZAA_1' : process_NZAA_1,
               'NZAA_2' : process_NZAA_2
               }
    # run process from dd option
    if fc in options:
        options[fc]()
    else:
        print("No process for feaure class")
    



