import sys

def check_duplicate_lines(filename):
  #print(filename)
  f = open(filename)
  lines = f.readlines()

  copy_lines = []

  duplicated_lines = {}
  index_duplicated_lines = []

  index = 0

  for line in lines:
    line = line.rstrip()
    copy_lines.append(line)
    #sys.stdout.write(line+'\n')

  copy_lines2 = copy_lines

  for line in copy_lines:
    if line in copy_lines2[index+1:]:
      duplicate_line = line
      sys.stdout.write(line + ' is duplicated\n')
      duplicated_lines[duplicate_line] = duplicated_lines.get(duplicate_line,0) + 1
      index_duplicated_lines.append(index)
    index = index + 1

  n_duplicated_lines = len(duplicated_lines)
 
  if ( n_duplicated_lines > 0 ):
    print("There are " + str(len(duplicated_lines)) + " duplicated lines in " + filename + "\nBelow the list of them and how many times they are replicated")
  else:
    print("No duplicated lines in " + filename + " file")

  if ( n_duplicated_lines > 0 ):

    for duplicate_line in duplicated_lines:
      print(duplicate_line, '\t->\t', duplicated_lines[duplicate_line])

    print("Below the line number of duplicated lines (starting from 1)")

    for line in index_duplicated_lines:
      print("line " + str(line+1) + " is duplicated")




if ( __name__ == "__main__" ):
  if (len(sys.argv) != 2):
    print("Usage: %s <filename.txt>\n" % (sys.argv[0] ))
    exit(2)
  filename = sys.argv[1]
  check_duplicate_lines(filename)
