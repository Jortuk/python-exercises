#!/usr/bin/env python3

def lone_sum(a, b, c):
  sum = a + b + c
  if a == b and a == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == a:
    return c
  elif b == c:
    return a
  elif c == a:
    return b
  elif c == b:
    return a
  else:
    return sum