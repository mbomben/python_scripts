import sys
import numpy



def average(nums):
  nums=numpy.asarray(nums)
  av=numpy.mean(nums)
  return av

def RMS(nums):
  nums=numpy.asarray(nums)
  rms=numpy.var(nums,ddof=1)
  return numpy.sqrt(rms)

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 2 ):
    print "Usage:",sys.argv[0],"numbers\n";
    exit(2)
  alist = []
  alist = sys.argv[1]
  #print 'mean =',average(alist)
  #print 'rms  =',RMS(alist)
