import sys
from check_duplicate_lines import check_duplicate_lines as cdl

def trim_duplicated_lines(filename,verbose=0):
  
  new_filename = "new_" +filename

  # list of duplicated lines
  # Attention: the number of lines starts from 1 and not from 0
  list_of_duplicated_lines = cdl(filename,verbose)

  f = open(filename,'r')

  new_f = open(new_filename,'w')

  f_lines = f.readlines()

  n_lines = len(f_lines)

  for n_line in range(n_lines):
    if ( not ( (n_line+1) in list_of_duplicated_lines ) ):
      print(f_lines[n_line])

if ( __name__ == "__main__" ):
  if (len(sys.argv) < 2 or len(sys.argv) > 3):
    print("Usage: %s <filename.txt> (verbose=0)\n" % (sys.argv[0] ))
    exit(2)
  filename = sys.argv[1]
  verbose = 0
  if ( len(sys.argv) > 2 ):
    verbose = int(sys.argv[2])
  trim_duplicated_lines(filename,verbose)
