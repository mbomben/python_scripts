import sys

def format_E_Field(original_file, result_file):

  with open(original_file,'rb') as original:
    original_lines=original.readlines()

  all_z = []
  all_Ez = []
  new_lines = []
  for original_line in original_lines:
    tmp = original_line.split()
    z  = float(tmp[0])
    Ez = float(tmp[1])
    line = "0.0 0.0 {0:9.3e} 0.0 0.0 {1:9.3e}".format(z,Ez)
    new_lines.append(str(line))


  with open(result_file,'w') as ofile:
    for new_line in new_lines:
      ofile.write('%s\n' % (new_line))

if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print("Usage: %s ""<original file> <new results file>\n" % (sys.argv[0]))
    exit(2)
  original_filename = sys.argv[1]
  new_filename = sys.argv[2]
  format_E_Field(original_filename,new_filename)
  print("formatted file is: %s\n" % (new_filename))
