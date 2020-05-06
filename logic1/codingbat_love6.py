#!/usr/bin/env python3

def love6(a, b):
  sum = a + b 
  if a == 6 or b == 6:
    return True
  elif sum == 6:
    return True
  elif (a - b == 6) or (b - a == 6):
    return True
  else:
    return False