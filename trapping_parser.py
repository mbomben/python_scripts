import argparse
import sys

def trapping_parser(arguments): 

  parser = argparse.ArgumentParser(description='Calculate trapping constant.')
  parser.add_argument('--xml','-x',nargs=1, type=str, help='name of the radiation damage model xml file',required=True)
  parser.add_argument('--f_T','-i', nargs='+', type=str, help='Ionizing probabilities files',required=True)
  parser.add_argument('--velocities','-v', nargs=2, type=float, help='electron and hole velocities [cm/s]',required=True)
  parser.add_argument('--fluence','-f', nargs=1, type=float, help='fluence [1/cm^2]',required=True)
  parser.add_argument('--output','-o',nargs=1, type=str, help='name of the output file',required=True)


  args = parser.parse_args(arguments)
  return args

if ( __name__ == "__main__" ):
  args = trapping_parser(sys.argv[1:])
  print args
