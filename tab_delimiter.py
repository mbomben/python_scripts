import sys

def tab_delimiter(original_filename,line_number):
  line_number = int(line_number)
  with open(original_file,'rb') as original:
    original_lines=original.readlines()
  index = 1
  for line in original_lines:
    if (index < line_number ):
      continue
    tmp = original_line.split()
    fields = []
    for tmps in tmp:
      fields.append(float(tmp))
      fields.append('\t')
    fields.pop()
    print fields



if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print "Usage:",sys.argv[0],"<original file> <line number>"
    exit(2)
  original_filename = sys.argv[1]
  line_number  = sys.argv[2]
  tab_delimiter(original_filename,line_number)


