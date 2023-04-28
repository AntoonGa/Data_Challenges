# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:39:28 2023

@author: grab
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

def runningSum(nums):
    run_sum = []
    for ii in range(len(nums)):
        if ii == 0:
            run_sum.append(nums[ii])
        else:
            run_sum.append(run_sum[ii-1]+nums[ii])

    return run_sum

nums = [3,1,2,10,1]

print(runningSum(nums))