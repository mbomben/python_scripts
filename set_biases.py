#!/usr/bin/env python3
import fileinput
import sys

def set_biases(name):
  fileToSearch=name
  
  
  biases=[]
  with open(fileToSearch,'r') as f:
    for l in f:
      #print l,
      biases.append(float(l))
  
  #print biases
  bias0 = 0
  biases.insert(bias0,0)
  #print biases
  delta_biases = []
  n = len(biases)
  for i in range(1,n):
    delta_biases.append(biases[i]-biases[i-1])
  #print delta_biases
  steps = []
  for db in delta_biases:
    steps.append(db/10)
  #print steps
  
  biases.pop(0)
  nbiassteps= len(biases)
  print "set nbiassteps=",nbiassteps
  final_string = "assign name = final n.val= ("
  for bias in biases:
    final_string = final_string + str(bias) + ","
  final_string = final_string[:-1]
  final_string = final_string +")"
  print final_string
  
  steps_string = "assign name = steps n.val= ("
  for step in steps:
    steps_string = steps_string + str(step) + ","
  steps_string = steps_string[:-1]
  steps_string = steps_string +")"
  print steps_string
  
if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) > 2 ):
    print "Usage:",sys.argv[0],"[<filename>]\n";
    exit(2)
  name="bias.txt"
  if (len(sys.argv) == 2 ):
    name = sys.argv[1]
  set_biases(name)
