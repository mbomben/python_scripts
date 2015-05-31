import sys


def write_ratio(filename1,filename2,savefile):

  max_diff = 1e-6

  input_file1 = open(filename1,'r')
  input_file2 = open(filename2,'r')

  input_lines1 = input_file1.readlines()
  input_lines2 = input_file2.readlines()

  if ( len(input_lines1)!=len(input_lines2) ):
    print filename1,"and",filename2,"should have the same number of lines"
    return -1

  output_file = open(savefile,'w')

  nlines = len(input_lines1)

  results = []
  ratios  = []

  for line in range(nlines):
    tmp1 = input_lines1[line].split()
    tmp2 = input_lines2[line].split()
    tmp1_field1 = float(tmp1[0])
    tmp2_field1 = float(tmp2[0])
    asymm = abs(tmp1_field1-tmp2_field1)/(tmp1_field1+tmp2_field1)
    if (asymm > max_diff):
      print "lines #",(line+1),"differ more than",max_diff,":",asymm
      return -2
    tmp1_field2 = float(tmp1[1])
    tmp2_field2 = float(tmp2[1])
    assert(tmp2_field2)
    ratio = tmp1_field2/tmp2_field2
    output_file.write('%f %e\n' % (tmp1_field1, ratio))
    results.append(tmp1_field1)
    ratios.append(ratio)

if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print "Usage:",sys.argv[0],"<filename1> <filename2> <savefile>"
    exit(2)
  filename1 = sys.argv[1]
  filename2 = sys.argv[2]
  savefile  = sys.argv[3]
  write_ratio(filename1,filename2,savefile)
