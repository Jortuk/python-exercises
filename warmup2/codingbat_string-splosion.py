#!/usr/bin/env python3

def string_splosion(str):
  n = 0
  newstr = ""
  for i in range(len(str)):
    n += 1
    newstr = newstr + str[:n]
  return newstr