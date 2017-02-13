import os
from time import sleep
import sys

def check_for_processes():
  # checking how many pgrep and atlas jobs are around
  atlas_jobs = os.popen("pgrep atlas").read()
  deckbuild_jobs = os.popen("pgrep deckbuild").read()
  # the output is in a string format; using split to get a list
  list_of_atlas_jobs = atlas_jobs.split()
  list_of_deckbuild_jobs = deckbuild_jobs.split()
  # number of atlas and deckbuild jobs
  n_of_atlas_jobs = len(list_of_atlas_jobs)
  n_of_deckbuild_jobs = len(list_of_deckbuild_jobs)
  print "n_of_atlas_jobs =",n_of_atlas_jobs
  print "n_of_deckbuild_jobs =",n_of_deckbuild_jobs
  return n_of_atlas_jobs+n_of_deckbuild_jobs

def submit_tcad_jobs( cmd, priority=0 ):
  print "command received is",cmd
  # variable to account for how many times within timeout time 
  # no atlas and deckbuild jobs where found
  n_of_valid_conditions = 0
  # minimal number of times valid conditions have to be met to run
  min_n_of_valid_conditions_met = 2
  # timeout time for checking processes (in seconds)
  check_timeout_time = 5*60 # 5 minutes
  # timeout time for verification of checking processes (in seconds)
  verification_timeout_time = 1*60 # 1 minute
  # number of running processes 
  n_processes = 1 # starting value to have while condition starting

  while( n_processes ):
    sleep(check_timeout_time)
    n_processes = check_for_processes()
    print n_processes,"found"
    while ( n_processes == 0 and n_of_valid_conditions<min_n_of_valid_conditions_met):
      print n_processes,"found"
      n_of_valid_conditions = n_of_valid_conditions + 1
      sleep(verification_timeout_time)
      n_processes = check_for_processes()
      if ( n_processes == 0 ):
        n_of_valid_conditions = n_of_valid_conditions + 1
      else:
        n_of_valid_conditions = 0
        n_processes = 1
      if ( not(n_of_valid_conditions<min_n_of_valid_conditions_met)):
        result = os.popen(cmd).read()
        print result
        break



if (__name__ == "__main__"):
  if (len(sys.argv) <2):
    print "Usage:",sys.argv[0],"command [priority]"
    exit(2)
  cmd = sys.argv[1]
  submit_tcad_jobs( cmd, priority=1)


