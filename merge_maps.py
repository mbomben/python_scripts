import os
import sys

def file_exists(file_name):
  file_existence = os.path.exists(file_name)
  if not file_existence:
        print("%s does not exist" % (file_name))
  return file_existence

def get_file_size(file_name):
  file_size = os.path.getsize(file_name)
  if ( file_size == 0 ):
    print("%s has zero size" % (file_name))
  return file_size

def merge_maps(zmin,zmax,output_file_name):


  base_file_name = "map_2D_z_"
  Xextension = "_EFieldX.dat"
  Yextension = "_EFieldY.dat"
  Zextension = "_EFieldZ.dat"

  new_point = 1
  new_current = 2

  skipz = 0

  with open(output_file_name,'w') as ofile:
    for z in range(zmin,zmax+1):
      skipz = 0
      original_fileX = base_file_name + str(z) + Xextension
      original_fileY = base_file_name + str(z) + Yextension
      original_fileZ = base_file_name + str(z) + Zextension
      if ( not ( file_exists(original_fileX) and file_exists(original_fileY) and file_exists(original_fileZ) and get_file_size(original_fileX) and get_file_size(original_fileY) and get_file_size(original_fileZ) ) ):
        print("Skipping all files for z = %d" % (z))
        skipz = 1
      if not skipz:    
        with open(original_fileX,'r') as originalX:
          original_linesX = originalX.readlines()
        nlinesX = len(original_linesX)
        with open(original_fileY,'r') as originalY:
          original_linesY = originalY.readlines()
        nlinesY = len(original_linesY)
        with open(original_fileZ,'r') as originalZ:
          original_linesZ = originalZ.readlines()
        nlinesZ = len(original_linesZ)
        if ( ( not ( nlinesX == nlinesY ) ) or ( not ( nlinesZ == nlinesY ) ) ):
          print("Files for z = %d have different number of lines; skipping" % (z))
          skipz = 1
        if not skipz:
          for line_index in range(nlinesX):
            lineX = original_linesX[line_index]
            lineY = original_linesY[line_index]
            lineZ = original_linesZ[line_index]
            split_lineX = lineX.split()
            split_lineY = lineY.split()
            split_lineZ = lineZ.split()
            x = float(split_lineX[0])
            y = float(split_lineX[1])
            Ex = float(split_lineX[2])
            Ey = float(split_lineY[2])
            Ez = float(split_lineZ[2])
            ofile.write('%e %e %d %e %e %e\n' % (x,y,z,Ex,Ey,Ez))




if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print("Usage: %s ""<zmin> <zmax> <output file name>\n" % (sys.argv[0]))
    exit(2)
  zmin = int(sys.argv[1])
  zmax  = int(sys.argv[2])
  output_file_name  = sys.argv[3]
  merge_maps(zmin,zmax,output_file_name)
  print("merged file is: %s\n" % (output_file_name))  
