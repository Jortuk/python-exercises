#!/usr/bin/env python3

def array_front9(nums):
  front = nums[0:4]
  for i in front:
    if i == 9:
      return True
  else:
    return False