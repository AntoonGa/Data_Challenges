"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Method:
    find all substring of given length N -> 1.
    check if any substring is palindrome
        if palindrome: break and return
        else: continue
    
Issue:
    the code is currently too slow for long string input
    possible improvement: instead of gathering all substring of given size
    we can check substring for palindrome individually
"""


def longestPalindrome(s: str) -> str:
    
    def find_substrings(s: str, n: int) -> [str]:
        """Find all substring of size n in string s"""

        # Create an empty list to store the substrings
        substrings = []

        # Loop through the string, starting at index 0
        for i in range(len(s)):
            # Check if the current index is less than M - N (the maximum index for a substring of length N)
            if i < len(s) - n + 1:
                # Get the substring of length N starting at the current index
                substring = s[i : i + n]
                # Add the substring to the list of substrings
                substrings.append(substring)

        # Return the list of substrings
        return substrings

    def is_palindrome(s: str) -> bool:
        """Check if input s is palindrome"""
        # If the input string is empty, return True (an empty string is considered a palindrome)
        if not s:
            return False

        if s == s[::-1]:
            return True
        else:
            return False

    """main"""
    palindrome = ""
    exit_flag = False

    # Range start from max to min size of substrings
    for ii in range(len(s), 0, -1):
        # Stop loop if palindrome is found: no longer palindrome can exits
        if exit_flag == True:
            break

        else:
            str_list = find_substrings(s, ii)
            for elem in str_list:
                if is_palindrome(elem):
                    palindrome = elem
                    exit_flag = True

    return palindrome


# s = 'aaaaa'
# s = "bababazeazea"
s = "tazeradartaweaweazer"
print(longestPalindrome(s))
