# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Created on Tue Dec 13 09:16:38 2022

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

@author: grab
"""


def lengthOfLongestSubstring(s: str) -> int:

    # empty string returns 0
    if s == "":
        len_longest = 0

    else:
        # default is single char len
        len_longest = 1

        # iterate through starting elem
        for ii in range(len(s)):
            # initiate list of char with no common char
            char_list = [s[ii]]
            len_char_list = len(char_list)

            # iterate through rest of elem
            for jj in range(ii + 1, len(s)):
                # check if not in common char list
                if s[jj] not in char_list:
                    char_list.append(s[jj])
                    len_char_list += 1
                else:
                    break
            # check if char list is longer than w/ previous starting ii
            if len(char_list) > len_longest:
                len_longest = len_char_list

    return len_longest

s = "abcdd"
lengthOfLongestSubstring(s)
