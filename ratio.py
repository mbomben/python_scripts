
import sys
x1  = float(sys.argv[1])
x2  = float(sys.argv[2])
x   = 0
try:
      x = x1/x2
      print (x)
except ValueError:
      print "You should have given either an int or a float"
except ZeroDivisionError:
      print "Infinity"
