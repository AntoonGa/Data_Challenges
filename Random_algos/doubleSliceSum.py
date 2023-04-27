# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:47:56 2023

@author: grab
"""

"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

"""

A = [3,2,6,-1,4,5,-1,2]
n = len(A)

forward_sum = [0] * n
backward_sum = [0] * n

for ii in range(n): #O(n)
    if ii == 0:
        continue
    else:
        forward_sum[ii] += forward_sum[ii - 1] + A[ii]
        if forward_sum[ii] < 0:
            forward_sum[ii] = 0
            
for ii in range(n-1, -1, -1):  #O(n)
    if ii == n-1:
        continue
    else:
        backward_sum[ii] += backward_sum[ii + 1] + A[ii]
        if backward_sum[ii] < 0:
            backward_sum[ii] = 0            

# search
best_value = -1e10
best_y = 100
for y in range(1,n-2):  #O(n)
    curr_value = forward_sum[y-1] + backward_sum[y+1]
    if curr_value >= best_value:
        best_value = max(best_value, curr_value)
        best_y = y
        
    