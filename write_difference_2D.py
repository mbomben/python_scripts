import sys


def write_difference_2D(filename1,filename2,savefile):

  max_diff = 1e-6

  input_file1 = open(filename1,'r')
  input_file2 = open(filename2,'r')

  input_lines1 = input_file1.readlines()
  input_lines2 = input_file2.readlines()

  if ( len(input_lines1)!=len(input_lines2) ):
    print(filename1+" and " + filename2 + " should have the same number of lines")
    return -1

  output_file = open(savefile,'w')

  nlines = len(input_lines1)

  results = []
  differences  = []

  for line in range(nlines):
    tmp1 = input_lines1[line].split()
    tmp2 = input_lines2[line].split()
    tmp1_field1 = float(tmp1[0])
    tmp2_field1 = float(tmp2[0])
    tmp1_field2 = float(tmp1[1])
    tmp2_field2 = float(tmp2[1])
    if ( tmp1_field1 == 0 and tmp2_field1 == 0 ):
      1+1
    else:
      asymm = abs(tmp1_field1-tmp2_field1)/(tmp1_field1+tmp2_field1)
      if (asymm > max_diff):
        print("lines #" +str(line+1) + " differ more than ",str(max_diff) + ":" +str(asymm))
        return -2
    if ( tmp1_field2 == 0 and tmp2_field2 == 0 ):
      1+1
    else:
      asymm = abs(tmp1_field2-tmp2_field2)/(tmp1_field2+tmp2_field2)
      if (asymm > max_diff):
        print("lines #" +str(line+1) + " differ more than ",str(max_diff) + ":" +str(asymm))
        return -2
    tmp1_field3 = float(tmp1[2])
    tmp2_field3 = float(tmp2[2])
    #assert(tmp2_field2)
    difference = tmp1_field3-tmp2_field3
    output_file.write('%e %e %e\n' % (tmp1_field1, tmp1_field2, difference))
    results.append([tmp1_field1,tmp1_field2])
    differences.append(difference)

if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print("Usage: "+sys.argv[0]+" <filename1> <filename2> <savefile>")
    exit(2)
  filename1 = sys.argv[1]
  filename2 = sys.argv[2]
  savefile  = sys.argv[3]
  write_difference_2D(filename1,filename2,savefile)
