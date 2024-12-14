import arcpy

import arcpy.mapping
arcpy.env.workspace=r"E:\pallabi\input"

arcpy.env.overwriteOutput=True

shape_data=arcpy.ListFeatureClasses()

print (shape_data)
point_data=r"E:\pallabi\input\buildings.shp"
road=r"E:\pallabi\input\roads.shp"
buffer_distance="100 Meters"
buffer_output=r"E:\pallabi\output\point_buffer\point_buffer_out.shp"
arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option="ALL")
pdf_output=r"E:\pallabi\buffermapoutput\buildingsmap.pdf"
mxd_path=r'E:\pallabi\map\blankmap.mxd'
intersect_out=r"E:\pallabi\output\intersection\intersect_out.shp"
arcpy.Intersect_analysis([buffer_output,road],intersect_out)
print("Intersection Analysis Successful")
mxd=arcpy.mapping.MapDocument(mxd_path)
df=arcpy.mapping.ListDataFrames(mxd)[0]
buffer_layer=arcpy.mapping.Layer(buffer_output)
point_Layer=arcpy.mapping.Layer(buffer_output)
arcpy.mapping.AddLayer(df,point_Layer,add_position="TOP")
Intersection_layer=arcpy.mapping.Layer(intersect_out)
arcpy.mapping.AddLayer(df,Intersection_layer,add_position="TOP")
arcpy.mapping.ExportToPDF(mxd,pdf_output)

