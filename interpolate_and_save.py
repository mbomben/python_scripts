import pandas as pd
import numpy as np
from scipy.interpolate import splrep, splev
import argparse
import os
import sys

# argument parser
def argumentParser(arguments):
  parser = argparse.ArgumentParser()
  parser.add_argument("--input",help="input file",required=True)
  parser.add_argument("--points",help="points file",required=True)
  parser.add_argument("--output",help="output file",required=True)
  parser.add_argument('--noheaders', action='store_true', help="Are there no headers? (default: no/False)")

  args = parser.parse_args(arguments)


  return args



def interpolate_and_save(data_file,headers, grid_file, output_file):
    try:
        # 1. Load Data: sep=None detects commas, tabs, or spaces automatically
        df = pd.read_csv(data_file, header=headers, skip_blank_lines=True, sep=None, engine='python')
        
        # 2. Clean Data: Remove headers/text and drop rows with NaN
        df = df.apply(pd.to_numeric, errors='coerce').dropna()
        df.columns = ['x', 'y']
        
        # 3. Handle Duplicates & Sort: 
        # splrep requires strictly increasing X. We average Y for duplicate X.
        df = df.groupby('x').mean().reset_index().sort_values('x')
        
        # 4. Load Target Grid: Single column of X values
        grid_df = pd.read_csv(grid_file, header=None, skip_blank_lines=True)
        target_x = pd.to_numeric(grid_df.iloc[:, 0], errors='coerce').dropna()

        # 5. Perform Interpolation
        # s=0 ensures the spline passes exactly through your data points
        tck = splrep(df['x'], df['y'], s=0)
        interpolated_y = splev(target_x, tck)

        # 6. Prepare and Save Output
        result = pd.DataFrame({
            'x': target_x,
            'y': interpolated_y
        })

        # sep=' ' for space separation
        # float_format='%.10e' ensures scientific notation (e.g., 1.2345678901e+02)
        result.to_csv(output_file, 
                      sep=' ', 
                      index=False, 
                      header=False, 
                      float_format='%.5e')
        
        print(f"File successfully saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if ( __name__ == "__main__" ):
  args = argumentParser(sys.argv[1:])
  data_file = args.input
  print(data_file)
  grid_file = args.points
  print(grid_file)
  output_file = args.output
  noheaders = args.noheaders
  headers = not(noheaders)
  if ( headers ):
    headers = 0
  else:
    headers = None
  interpolate_and_save(data_file,headers,grid_file,output_file)
