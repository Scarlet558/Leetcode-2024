"""
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false


Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        num_map = {
            "0" : "0",
            "1" : "1",
            "6" : "9",
            "8" : "8",
            "9" : "6"
        }

        rotated_str = []

        for char in reversed(num):
            if char not in num_map:
                return False
            else :
                rotated_str.append(num_map[char])
        rotated_string = ''.join(rotated_str)
        return rotated_string == num

num = "69"
print(Solution().isStrobogrammatic(num))