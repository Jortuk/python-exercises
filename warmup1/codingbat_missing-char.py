#!/usr/bin/env python3

def missing_char(str, n):
  startstr = str[:n]
  endstr = str[n+1:]
  return startstr + endstr