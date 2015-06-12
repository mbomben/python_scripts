import argparse

def parser(arguments): 

  parser = argparse.ArgumentParser(description='Prepare deck file.')
  parser.add_argument('--template',nargs=1, type=str, help='name of the template deck file',required=True)
  #parser.add_argument('--entry_point','-i', nargs=2, metavar=('x', 'y'), help='track entry point',required=True)
  #parser.add_argument('--exit_point','-o', nargs=2, metavar=('x', 'y'), help='track exit point',required=True)
  parser.add_argument('--pitch','-p', nargs=1, type=float, help='pixel pitch [um]',required=True)
  parser.add_argument('--thickness','-w', nargs=1, type=float, help='pixel thickness [um]',required=True)
  parser.add_argument('--npixels','-n', nargs=1, type=int, help='number of pixels simulated',required=True)
  parser.add_argument('--deltay','-y', nargs=1, type=float, help='trackin resolution [um]',required=True)


  args = parser.parse_args(arguments)
  return args
