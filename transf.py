x , y = -112.0, 13.0
crs = QgsCoordinateReferenceSystem(4326) # wgs84
crsnuevo = QgsCoordinateReferenceSystem(26912) # NAD 83 / UTM Zpne 12
trform =  QgsCoordinateTransform(crs, crsnuevo, QgsProject.instance())
ptutm = trform.transform(QgsPointXY(x , y))
print("punto utm:", ptutm)
ptwgs = trform.transform(ptutm, QgsCoordinateTransform.ReverseTransform)
print("punto wgs:", ptwgs)
