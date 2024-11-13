"""
Given a string s, return true if a permutation of the string could form a  palindrome false otherwise.


Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""
"""

Problem Approach:

Key Insight: For a string to form a palindrome, it can have at most one character with an odd frequency count

Even length palindrome: all characters must appear even times
Odd length palindrome: exactly one character can appear odd times (middle character)


Solution Steps:

Count frequency of each character using Counter
Count how many characters appear odd number of times
Return true if odd count ≤ 1, false otherwise

"""

import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_count = collections.Counter(s)
        count = 0


        for idx, val in s_count.items():
            if val % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True

s = Solution()
print(s.canPermutePalindrome("carerac"))