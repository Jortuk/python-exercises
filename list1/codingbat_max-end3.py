#!/usr/bin/env python3

def max_end3(nums):
  if nums[0] > nums[2]:
    list1 = []
    list1.append(nums[0])
    list1.append(nums[0])
    list1.append(nums[0])
    return list1
  else:
    list2 = []
    list2.append(nums[2])
    list2.append(nums[2])
    list2.append(nums[2])
    return list2

    # OR

def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums