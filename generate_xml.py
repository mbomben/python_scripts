import sys


def generate_xml(name,n):
  name = str(name)
  n = int(n)
  print("name = %s" %(name))
  print("n = %d" %(n))

  header = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>

  <plot 
  xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
  xsi:noNamespaceSchemaLocation=\"root_multi_graph.xsd\">"""

  filename = """<filename>                </filename>"""
  title = """<title>                                       </title>"""
  legend = """<legend>
      <x1>0.2</x1>
      <y1>0.7</y1>
      <x2>0.4</x2>
      <y2>0.89</y2>
    </legend>"""
  axes = """
  <axe>
      <name>X</name>
      <label>                 </label>
      <min> </min>
      <max>   </max>
      <log>0</log>
    </axe>
    <axe>
      <name>Y</name>
      <label>                               </label>
      <min>     </min>
      <max>      </max>
      <log>0</log>
    </axe>"""
  curve = """
    <curve>
    <data>                    </data>
    <label>                   </label>
    <marker>
      <style>  </style>
      <color> </color>
      <size>1.2</size>
    </marker>
    <line>
      <size>1</size>
      <color> </color>
      <style>1</style>
    </line>
  </curve>"""

  
  footer = """</plot>"""

  with open(name,"w") as f:
    f.write(header)
    f.write("\n")
    f.write(filename)
    f.write("\n")
    f.write(title)
    f.write("\n")
    f.write(legend)
    f.write(axes) 
    f.write("\n")
    for i in range(n):
      dummy = curve
      markerstyle = 20+i
      color  = i+1

      newmarkersyle ="<style>"+str(markerstyle)+"</style>" 
      newcolor      ="<color>"+str(color)+"</color>" 
      dummy  = dummy.replace("<style>  </style>",newmarkersyle,14)
      dummy  = dummy.replace("<color> </color>",newcolor     ,14)
      f.write(dummy)

    f.write("\n")
    f.write(footer)
    f.write("\n")

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) != 3 ):
    print("Usage: %s <filename.xml> <number of curves>" % (sys.argv[0]));
    exit(2)
  name = sys.argv[1]
  n = int(sys.argv[2])
  if ( n > 15 ):
    print("Too many curves, not enough markers")
    exit( 2 )
  generate_xml(name,n)
