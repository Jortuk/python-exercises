#!/usr/bin/env python3

def parrot_trouble(talking, hour):
  if hour < 7 and talking is True:
    return True
  elif hour > 20 and talking is True:
    return True
  else:
    return False 
