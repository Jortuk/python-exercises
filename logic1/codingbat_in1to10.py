#!/usr/bin/env python3

def in1to10(n, outside_mode):
  if outside_mode and (n <= 1 or n >= 10):
    return True
  elif outside_mode:
    return False
  if n in range(1, 10 + 1):
    return True
  else:
    return False
