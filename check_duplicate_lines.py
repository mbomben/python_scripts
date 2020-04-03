import sys

def check_duplicate_lines(filename,verbose=0):
  #print(filename)
  f = open(filename)
  lines = f.readlines()

  copy_lines = []

  duplicated_lines = {}
  index_duplicated_lines = []


  for line in lines:
    line = line.rstrip()
    copy_lines.append(line)
    #sys.stdout.write(line+'\n')

  copy_lines2 = copy_lines

  n_lines = len(copy_lines)
  #print(n_lines)

  for iline in range(n_lines):
    if ( iline != n_lines-1 ):
      for iline2 in range(iline+1,n_lines):
        str1 = copy_lines[iline]
        str2 = copy_lines2[iline2]
        if ( str2 == str1 ):
          if ( not (iline2 in index_duplicated_lines) ):
            if ( verbose ): 
              sys.stdout.write(str2 + ' is duplicated\n')
            duplicated_lines[str2] = duplicated_lines.get(str2,0) + 1
            index_duplicated_lines.append(iline2)

  n_duplicated_lines = len(duplicated_lines)
 
  if ( verbose ): 
    if ( n_duplicated_lines > 0 ):
      print("There are " + str(len(duplicated_lines)) + " duplicated lines in " + filename + "\nBelow the list of them and how many times they are replicated")
    else:
      print("No duplicated lines in " + filename + " file")

    if ( n_duplicated_lines > 0 ):

      for duplicate_line in duplicated_lines:
        print(duplicate_line, '\t->\t', duplicated_lines[duplicate_line])

      print("Below the line number of duplicated lines (starting from 1)")

      for line in sorted(index_duplicated_lines):
        print("line " + str(line+1) + " is duplicated")

  return [i+1 for i in sorted(index_duplicated_lines)]  


if ( __name__ == "__main__" ):
  if (len(sys.argv) < 2 or len(sys.argv) > 3):
    print("Usage: %s <filename.txt> (verbose=0)\n" % (sys.argv[0] ))
    exit(2)
  filename = sys.argv[1]
  verbose = 0
  if ( len(sys.argv) > 2 ):
    verbose = int(sys.argv[2])
  sorted_index_duplicated_lines = check_duplicate_lines(filename,verbose)
