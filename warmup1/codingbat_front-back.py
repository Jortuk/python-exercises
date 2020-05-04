#!/usr/bin/env python3

def front_back(str):
  newstr = str[-1:] + str[1:-1] + str[:1]
  if str is 'a':
    return str
  else:
    return newstr 