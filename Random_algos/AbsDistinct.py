"""
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
"""

A = [-100,-12,-11,0,1,2,3,3,4,5,6,7,8,9,10,11,12,12]
A = [-1,0,0,0,0,1]
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    #asserts types
    assert isinstance(A, list), "A must be list"
    #special cases
    n = len(A)
    if n == A: return 1

    ### Algo ###
    # result: nb disjoints elements in A (starts at 1 for first element!)
    counter = 1
    # force index shifting when same value is reached
    last_state = (-1,-1)
    # search indices: (start:end) of A
    ldx = 0
    rdx = n - 1
    
    # search loop
    while ldx < rdx:
        
        left = abs(A[ldx])
        right = abs(A[rdx])
                
        if left != right and last_state != (left, right):
            counter += 1
            
        if left > right:
            ldx += 1
        else:
            rdx += -1
            
        last_state = (left, right)

    return counter


print(solution(A))



