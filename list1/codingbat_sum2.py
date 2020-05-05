#!/usr/bin/env python3

def sum2(nums):
  if len(nums) < 2:
    total = sum(nums)
    return total
  elif nums == []:
    return 0
  else:
    answer = nums[0] + nums[1]
    return answer 