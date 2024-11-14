"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        """

        # s = "abc", t = "ahbgdc"

        s_ptr = 0
        t_ptr = 0

        # if len(s) > len(t):
        #     return False

        while t_ptr < len(t) and s_ptr < len(s):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

        return s_ptr == len(s)


s = Solution()
print(s.isSubsequence("axc", "axhbgd"))


