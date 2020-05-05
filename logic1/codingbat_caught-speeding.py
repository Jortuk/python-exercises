#!/usr/bin/env python3

def caught_speeding(speed, is_birthday):
  if is_birthday and speed <= 65:
      return 0
  elif is_birthday and speed <= 85:
    return 1
  elif speed <= 60:
    return 0
  elif speed >= 61 and speed <= 80:
    return 1
  elif speed >= 81:
    return 2