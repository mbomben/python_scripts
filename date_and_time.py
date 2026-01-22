from datetime import datetime


def date_and_time():
  # datetime object containing current date and time
  nowtime = datetime.now()
 

  # YYMMDD-HMS
  dt_string = nowtime.strftime("%y%m%d-%H%M%S")
  #print("date and time =", dt_string)
  
  return dt_string

if ( __name__ == "__main__" ):
  dt_string = date_and_time()
  print(dt_string)
