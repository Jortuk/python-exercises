#!/usr/bin/env python3

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  elif not a_smile and b_smile:
    return False
  elif a_smile and not b_smile:
    return False