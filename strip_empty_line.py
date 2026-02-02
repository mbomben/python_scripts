import argparse
import sys

# argument parser
def argumentParser(arguments):
  parser = argparse.ArgumentParser()
  parser.add_argument("--input",help="input file names",required=True)

  args = parser.parse_args(arguments)

  return args


def strip_empty_line(filename):

  with open(filename) as f_input:
    data = f_input.read().rstrip('\n')

  with open(filename, 'w') as f_output:    
    f_output.write(data)


if (__name__ == "__main__"):
  args = argumentParser(sys.argv[1:])
  input_file_name  = args.input
  #print(output_file_name)
  #print(noheaders)
  strip_empty_line(input_file_name)
