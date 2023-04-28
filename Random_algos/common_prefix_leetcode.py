# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-common-prefix/description/
Created on Mon Dec 12 15:12:50 2022

@author: grab

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

def longestCommonPrefix(strs: [str]) -> str:

    # If the input array is empty, return an empty string
    if not strs:
        return ""

    # We will iterate through the first string in the array, character by character,
    # and check if the character at the same position in all the other strings matches.
    # If it does, we will add the character to the common prefix string.
    # If it doesn't, we will stop and return the common prefix string we have built so far.

    # Initialize the common prefix string to be the empty string
    common_prefix = ""

    # Get the first string in the array
    first_str = strs[0]

    # Iterate through the first string character by character
    for i in range(len(first_str)):
        # Get the character at the current position
        c = first_str[i]

        # Iterate through the rest of the strings in the array
        for j in range(1, len(strs)):
        # Get the current string
            current_str = strs[j]

        # If the current string is shorter than the common prefix string
        # we have built so far, or the character at the current position
        # in the current string does not match the character in the common
        # prefix string, we stop and return the common prefix string
            if i >= len(current_str) or current_str[i] != c:
                return common_prefix

        # If we have reached this point, it means that the character at the
        # current position in the first string is present in all the other
        # strings at the same position, so we add it to the common prefix string
        common_prefix += c

    # If we have reached this point, it means that we have iterated through
    # the entire first string, and all the characters in the first string
    # are present in all the other strings at the same position, so the
    # common prefix is the entire first string
    return common_prefix
    
list1 = ["flower","flow","flight"]
print(longestCommonPrefix(list1)) 
    
