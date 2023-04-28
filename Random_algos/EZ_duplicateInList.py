# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:03:28 2023

@author: grab
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


def containsDuplicate(nums) -> bool:
    unique_set = set(nums)
    
    if len(unique_set) != len(nums):
        duplicate_bool = True
    else:
        duplicate_bool = False

    return duplicate_bool


nums = [1,1,1000,120]

print(containsDuplicate(nums))
