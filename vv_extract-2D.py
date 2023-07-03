import argparse
import sys
import os.path
import re

# argument parser
def argumentParser(arguments):
  parser = argparse.ArgumentParser()
  parser.add_argument("--template",help="extract template file",required=True)
  parser.add_argument("--TwoDname",help="2d map output file name",required=True)
  parser.add_argument("--ThreeDname",help="3d map input file name",required=True)
  parser.add_argument("--zmin",help="zmin",type=int,required=True)
  parser.add_argument("--zmax",help="zmax",type=int,required=True)


  args = parser.parse_args(arguments)


  return args




if (__name__ == "__main__" ):
  args = argumentParser(sys.argv[1:])
  #print(args.TwoDname)

  # we now write a series of extract files, one per z value
  # between zmin and zmax
  # the program will also print out a series of commands for tonyplot3d to extract the 2d maps

  # getting the arguments into variables
  # extract template file
  templateFileName = args.template
  #print(templateFileName)
  #print(baseSetFileName)
  # 2D map name
  map2Dname = args.TwoDname
  # 3D map name
  map3Dname = args.ThreeDname
  # zmin 
  zmin = args.zmin
  #print(zmin)
  # zmax 
  zmax = args.zmax
  #print(zmax)

  # preparing the different components of the filenames to be handled

  (dirName, fileName) = os.path.split(templateFileName)
  (fileBaseName, fileExtension)=os.path.splitext(fileName)
  #print (dirName)   
  #print (fileName)  
  #print (fileBaseName)    
  #print (fileExtension) 

  # keywords to be searched in the set template file
  loadHeader = "LOAD in=" 
  offsetHeader = "offset="
  saveHeader = "SAVE out="
  fileNameHeader = "file_name c.val="

  # open set template file for reading

  with open(templateFileName) as fin:
    inputLines = fin.readlines()
  #print(inputLines)

  # printing the command used to run the program
  print("#File produced using the following command:")
  print(("#python %s %s") % (sys.argv[0],(' '.join(f'--{k} {v}' for k, v in vars(args).items()))))

  # loop over all the z values to write out all the cut files and print the commands to run 
  # the projections to planes at fixed z value

  for z in range(zmin,zmax+1):
    # the 2D output file name
    map2DnameFileName = map2Dname + '_z' + str(z) + '.str'
    #print(map2DnameFileName)
    # extract file name
    extractFileName = fileBaseName + '_z' + str(z) + fileExtension
    #print(extractFileName)
    # output file name of the extraction
    ouputExtractFileName = extractFileName.replace(".in",".out")
    # open the set file in write mode
    with open(extractFileName,'w') as fout:
      # read each line of the set template file
      for inputLine in inputLines:
        # look for keywords:
        # first is LOAD header
        if (re.search(loadHeader,inputLine)):
          #print(("%s found in %s") % (pointHeader,inputLine))
          # write the point_ position with the z coordinate
          fout.write(("%s %s\n") % (inputLine.rstrip(),map3Dname))
        # second is the offset header
        elif(re.search(offsetHeader,inputLine)):
          fout.write(("%s %d\n") % (inputLine.rstrip(),z))
        # third is the SAVE header
        elif(re.search(saveHeader,inputLine)):
          fout.write(("%s %s\n") % (inputLine.rstrip(),map2DnameFileName))
        # fourth is the fileName header
        elif(re.search(fileNameHeader,inputLine)):
          fileName=map2DnameFileName.replace('.str','')
          fout.write(("%s %s\n") % (inputLine.rstrip(),fileName))
        # all other kid of lines - i.e. containing no keywords - will be just copied  
        else:
          fout.write(inputLine)
    print(("deckbuild -run %s -outfile %s") % (extractFileName,ouputExtractFileName))

