def direct_func( z, theta, y0 ):
  import math
  y = y0+z/math.tan(theta)
  return y
  
def inverse_func( y, theta, y0 ):
  import math
  z = (y-y0)*math.tan(theta)
  return z
 
def y0min_func( W, P, theta, dy ):
  import math
  tan_theta = math.tan(theta)
  y0min = -P/2+dy-W/tan_theta
  return y0min 
