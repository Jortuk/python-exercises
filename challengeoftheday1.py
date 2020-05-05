#!/usr/bin/env python3
import math

for num in range(1999,3201):
    if num %7 == 0 and num %5 != 0:
        print (num, end=',')
