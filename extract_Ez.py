import math

def extract_Ez():

  # input file names
  inputFileNames = {"fieldX" : "E_FieldX.dat", "fieldY" : "E_FieldY.dat", "fieldN" : "E_Field.dat"}
  #for key in inputFileNames:
  #  print(key,inputFileNames[key])

  # read input files
  fieldX_lines = []
  fieldY_lines = []
  fieldN_lines  = []

  fieldX_file = open(inputFileNames["fieldX"],"r")
  fieldY_file = open(inputFileNames["fieldY"],"r")
  fieldN_file = open(inputFileNames["fieldN"],"r")

  fieldX_lines = fieldX_file.readlines()
  fieldY_lines = fieldY_file.readlines()
  fieldN_lines = fieldN_file.readlines()

   
  inputFileLines = {"fieldX" : fieldX_lines, "fieldY" : fieldY_lines, "fieldN" : fieldN_lines}
  #for key in inputFileLines:
  #  print(key,len(inputFileLines[key]))
  
  # calculate the Ez value and write it to a new file
  outputFileName = "new_E_FieldZ.dat"
  with open("new_E_FieldZ.dat", "w") as outputFile:
    for index, fieldX_line in enumerate(fieldX_lines):
      fieldY_line = fieldY_lines[index]
      fieldN_line = fieldN_lines[index]
      tmpX = fieldX_line.split()
      tmpY = fieldY_line.split()
      tmpN = fieldN_line.split()
      #if ( index % 100000 == 0 ):
      #  print(index,type(fieldX_line),type(tmpX[3]))
      Ex = float(tmpX[3])
      Ey = float(tmpY[3])
      En = float(tmpN[3])
      Ez = math.sqrt(math.pow(En,2.0)-math.pow(Ex,2.0)-math.pow(Ey,2.0))
      # crosscheck if coordinates are consistent
      prec = 1e-12
      xx = float(tmpX[0])
      xy = float(tmpX[1])
      xz = float(tmpX[2])
      yx = float(tmpY[0])
      yy = float(tmpY[1])
      yz = float(tmpY[2])
      nx = float(tmpN[0])
      ny = float(tmpN[1])
      nz = float(tmpN[2])
      # flag to check error
      coordinatesConsistent = True
      if ( abs(xx-yx) > prec ):
        coordinatesConsistent = False
        print(index,xx,yx)
      if ( abs(xx-nx) > prec ):
        coordinatesConsistent = False
        print(index,xx,nx)
      if ( abs(xy-yy) > prec ):
        coordinatesConsistent = False
        print(index,xy,yy)
      if ( abs(xy-ny) > prec ):
        coordinatesConsistent = False
        print(index,xy,ny)
      if ( abs(xz-yz) > prec ):
        coordinatesConsistent = False
        print(index,xz,yz)
      if ( abs(xz-nz) > prec ):
        coordinatesConsistent = False
        print(index,xz,nz)
      #if ( index % 100000 == 0 ):
      #  print(index,En,Ez)
      if ( coordinatesConsistent ):
        result = "{xx} {xy} {xz} {Ez}\n".format(xx=xx,xy=xy,xz=xz,Ez=Ez)
        outputFile.write(result)
  print("Output file is %s" % (outputFileName))

if (__name__ == "__main__" ):
  extract_Ez()
