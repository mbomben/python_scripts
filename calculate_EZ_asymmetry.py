oldFileName="E_FieldZ.dat" 
newFileName="new_E_FieldZ.dat"

asymmetryFileName="new_vs_old_E_FieldZ_asymmetry.txt"

oldFile = open(oldFileName)
newFile = open(newFileName)

oldFileLines = oldFile.readlines()
newFileLines = newFile.readlines()


with open(asymmetryFileName,"w") as outputFile:
	for index,oldLine in enumerate(oldFileLines):
		newLine = newFileLines[index]
		oldTmp = oldLine.split()
		newTmp = newLine.split()
		x = float(oldTmp[0])
		y = float(oldTmp[1])
		z = float(oldTmp[2])
		oldEz = float(oldTmp[3])
		newEz = float(newTmp[3])
		# calculating asymmetry
		den = (oldEz+newEz)/2.0
		#assert den != 0, f"number different from 0 expected, got: {den} at index {index} and position {x} {y} {z}"
		#assert den != 0, f"number different from 0 expected, got: {den}"
		assert den != 0
		num = newEz-oldEz
		asymm = num/den
		outputFile.write("%f %f %f %f\n" % (x,y,z,asymm))
