import re
import sys

def readAndWrite(template_file_name,index,entry_point,exit_point):
  
  appendix = '_'+str(index)+'.in'
  new_file_name = template_file_name.replace('.in',appendix)
  input_file = open(template_file_name,'r')
  output_file = open(new_file_name,'w')
  entry_x = entry_point[0]
  entry_y = entry_point[1]
  exit_x = exit_point[0]
  exit_y = exit_point[1]
  
  for input_line in input_file:
    searchsingleeventupset = re.search('singleeventupset',input_line)
    searchSEU = re.search('-SEU',input_line)
    if searchsingleeventupset:
      #print input_line
      new_entry_point="entry=\""
      new_entry_point += str(entry_x)
      new_entry_point += ","
      new_entry_point += str(entry_y)
      new_entry_point += "\""
      #print new_entry_point
      new_exit_point="exit=\""
      new_exit_point += str(exit_x)
      new_exit_point += ","
      new_exit_point += str(exit_y)
      new_exit_point += "\""
      #print new_exit_point
      new_seu = re.sub("entry=\"\d+\.?\d?,\d+\.?\d?\"",new_entry_point,input_line)
      new_seu = re.sub("exit=\"\d+\.?\d?,\d+\.?\d?\"",new_exit_point,new_seu)
      #print new_seu
      output_file.write(new_seu)
    
    elif searchSEU:
      new_seu_appendix = '-SEU_' 
      new_seu_appendix += str(index)
      new_seu = re.sub('-SEU',new_seu_appendix,input_line)
      output_file.write(new_seu)
    else:
      output_file.write(input_line)
  
  input_file.close()
  output_file.close()

