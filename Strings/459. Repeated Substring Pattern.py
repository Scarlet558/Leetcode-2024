"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = "abcabcabcabc"
        #s = "aabcaabcaabc"

        # Try all possible substring lengths
        # We only need to check up to n//2 since the substring
        # must repeat at least twice
        for i in range(1, s // 2 + 1):
            # The string length must be divisible by substring length
            if s % i == 0:
                # Extract substring of length i
                substring = s[:i]
                # Calculate number of repetitions needed
                repetitions = s // i
                # Check if this substring repeated creates our string
                if substring * repetitions == s:
                    return True

        return False

        #O(n)

        # # if string is empty
        # if not s:
        #     return False
        #
        # if len(s) == 1:
        #     return False
        #
        # concat = s + s
        #
        # middle_part = concat[1:-1]
        #
        # return s in middle_part
