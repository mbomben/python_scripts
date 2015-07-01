import sys
if (len(sys.argv) !=4):
  print "Usage",sys.argv[0],"<file_name> <implant_name> <output_file>";
  print "Example:",sys.argv[0],"doping_profile.txt PhosProfile doping_profile.in";
  exit(len(sys.argv))

file_name=str(sys.argv[1])
implant_name=str(sys.argv[2])
output_file=str(sys.argv[3])

with open(file_name) as f:
  lines=f.readlines()

with open(output_file,'w') as f:
  f.write("profile name=\"%s\" \\\n" % (implant_name))
  i = 0
  for l in lines:
    line=[]
    line=l.split()
    x=float(line[0])
    c=float(line[1])
    f.write("d.p=%f,%e " % (x,c))
    i = i + 1
    if ( (i%4) == 0 ):
      f.write("\\\n")



