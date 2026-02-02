import os
import sys
import argparse
import re


# argument parser
def argumentParser(arguments):
  parser = argparse.ArgumentParser()
  parser.add_argument("--input",help="input file names",required=True)
  parser.add_argument("--output",help="output file name",required=True)
  parser.add_argument('--noheaders', action='store_true', help="Are there no headers? (default: no/False)")

  args = parser.parse_args(arguments)


  return args

def file_exists(file_name):
  file_existence = os.path.exists(file_name)
  if not file_existence:
        print("%s does not exist" % (file_name))
  return file_existence

def csv2txt(input_file_name,output_file_name,headers):
  #print("csv2txt")
  # check if file exists
  if ( not file_exists(input_file_name) ):
    print("Input file %s does not exist.\n Exiting..." % (input_file_name))
    exit(-1)

  # read lines of input file
  with open(input_file_name) as f:
    inputLines = f.readlines()

  # open output file
  with open(output_file_name,"w") as g:
    # count number of lines 
    indexLine = 0
    for idx, inputLine in enumerate(inputLines):
      #print(inputLine)
      #print(indexLine)
      #print(headers)
      # if the file has headers, skip the first line
      #print(idx)
      if ( idx == 0 and headers ):
        #print("First line containing headers: %s" % (inputLine))
        continue
      else:
        tmp = inputLine.split(',')
        x = float(tmp[0])
        y = float(tmp[1])
        g.write("%f %e\n" % (x,y))

  print("Saved file is %s" % (output_file_name))

if __name__ == "__main__":
  args = argumentParser(sys.argv[1:])
  output_file_name  = args.output
  #print(output_file_name)
  input_file_name  = args.input
  #print(input_file_name)
  noheaders = args.noheaders
  #print(noheaders)
  if ( not noheaders ):
    print("Headers are present")
  else:
    print("No headers in %s\n" %(input_file_name));
  headers = not(noheaders)
  csv2txt(input_file_name,output_file_name,headers)

  

