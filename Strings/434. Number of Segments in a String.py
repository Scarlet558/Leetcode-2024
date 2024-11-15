"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1

Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s = "Hello, my name is     John"

        count=0

        for i in range(len(s)):
            if ( i == 0 or s[i-1] == ' ') and s[i] != ' ':
                count+=1

        return count


s = "Hello, my name is    John"
sol = Solution()
print(sol.countSegments(s))