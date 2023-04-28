# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:39:42 2023

@author: grab
53. Maximum Subarray
Medium
27.2K
1.2K
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
"""
this implementation does the following:
loop through element of array
    cumulative sum
    if cumulative sum is negative, we dump everything because if it useless to the sum
    else we keep summing
    
This is a linear complexity algo !
    """
    
def maxSubArray(nums) -> int:
    " using sliding windows, removing negative prefix !"
    max_sub = nums[0]
    cur_sum = 0

    for n in nums:
        # this is the prefix ! dump if negative. Prefix can be the previous sum!
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sub = max(max_sub, cur_sum)

    return max_sub

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))